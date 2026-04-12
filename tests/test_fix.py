import os
from unittest.mock import MagicMock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    from app.backend.routes.response import router

    app = FastAPI()
    app.include_router(router)
    return TestClient(app)


@pytest.mark.parametrize(
    "provider,expected_text,client_path",
    [
        ("openai", "hello from openai", "chat.completions.create"),
        ("anthropic", "hello from anthropic", "messages.create"),
    ],
)
def test_generate_uses_provider_from_env(client, provider, expected_text, client_path):
    env = {
        "MODEL_PROVIDER": provider,
        "MODEL_NAME": "test-model",
        "OPENAI_API_KEY": "openai-key",
        "ANTHROPIC_API_KEY": "anthropic-key",
    }

    with patch.dict(os.environ, env, clear=False):
        if provider == "openai":
            mock_client = MagicMock()
            mock_client.chat.completions.create.return_value = MagicMock(
                choices=[MagicMock(message=MagicMock(content=expected_text))]
            )
            with patch("app.backend.routes.response.OpenAI", return_value=mock_client) as openai_ctor, patch(
                "app.backend.routes.response.Anthropic"
            ) as anthropic_ctor:
                res = client.post("/api/response/generate", json={"prompt": "Say hi"})
                assert res.status_code == 200
                assert res.json()["response"] == expected_text
                openai_ctor.assert_called_once()
                anthropic_ctor.assert_not_called()
                mock_client.chat.completions.create.assert_called_once()
                _, kwargs = mock_client.chat.completions.create.call_args
                assert kwargs["model"] == "test-model"
                assert kwargs["messages"] == [{"role": "user", "content": "Say hi"}]
        else:
            mock_client = MagicMock()
            mock_client.messages.create.return_value = MagicMock(
                content=[MagicMock(text=expected_text)]
            )
            with patch("app.backend.routes.response.Anthropic", return_value=mock_client) as anthropic_ctor, patch(
                "app.backend.routes.response.OpenAI"
            ) as openai_ctor:
                res = client.post("/api/response/generate", json={"prompt": "Say hi"})
                assert res.status_code == 200
                assert res.json()["response"] == expected_text
                anthropic_ctor.assert_called_once()
                openai_ctor.assert_not_called()
                mock_client.messages.create.assert_called_once()
                _, kwargs = mock_client.messages.create.call_args
                assert kwargs["model"] == "test-model"
                assert kwargs["messages"] == [{"role": "user", "content": "Say hi"}]


@pytest.mark.parametrize("provider", ["openai", "anthropic"])
def test_generate_forwards_optional_parameters(client, provider):
    env = {
        "MODEL_PROVIDER": provider,
        "MODEL_NAME": "test-model",
        "OPENAI_API_KEY": "openai-key",
        "ANTHROPIC_API_KEY": "anthropic-key",
    }
    params = {"temperature": 0.3, "max_tokens": 64}

    with patch.dict(os.environ, env, clear=False):
        if provider == "openai":
            mock_client = MagicMock()
            mock_client.chat.completions.create.return_value = MagicMock(
                choices=[MagicMock(message=MagicMock(content="ok"))]
            )
            with patch("app.backend.routes.response.OpenAI", return_value=mock_client):
                res = client.post(
                    "/api/response/generate",
                    json={"prompt": "Say hi", "parameters": params},
                )
                assert res.status_code == 200
                _, kwargs = mock_client.chat.completions.create.call_args
                assert kwargs["temperature"] == 0.3
                assert kwargs["max_tokens"] == 64
        else:
            mock_client = MagicMock()
            mock_client.messages.create.return_value = MagicMock(
                content=[MagicMock(text="ok")]
            )
            with patch("app.backend.routes.response.Anthropic", return_value=mock_client):
                res = client.post(
                    "/api/response/generate",
                    json={"prompt": "Say hi", "parameters": params},
                )
                assert res.status_code == 200
                _, kwargs = mock_client.messages.create.call_args
                assert kwargs["temperature"] == 0.3
                assert kwargs["max_tokens"] == 64


@pytest.mark.parametrize("provider", ["openai", "anthropic"])
def test_stream_returns_sse_chunks(client, provider):
    env = {
        "MODEL_PROVIDER": provider,
        "MODEL_NAME": "test-model",
        "OPENAI_API_KEY": "openai-key",
        "ANTHROPIC_API_KEY": "anthropic-key",
    }

    with patch.dict(os.environ, env, clear=False):
        if provider == "openai":
            class Chunk:
                def __init__(self, text):
                    self.choices = [MagicMock(delta=MagicMock(content=text))]

            class Stream:
                def __aiter__(self):
                    async def gen():
                        yield Chunk("a")
                        yield Chunk("b")
                    return gen()

            mock_client = MagicMock()
            mock_client.chat.completions.create.return_value = Stream()
            with patch("app.backend.routes.response.OpenAI", return_value=mock_client):
                res = client.post("/api/response/stream", json={"prompt": "Say hi"})
                assert res.status_code == 200
                assert "data: a" in res.text
                assert "data: b" in res.text
        else:
            class Event:
                def __init__(self, text):
                    self.type = "content_block_delta"
                    self.delta = MagicMock(text=text)

            class Stream:
                def __aiter__(self):
                    async def gen():
                        yield Event("a")
                        yield Event("b")
                    return gen()

            mock_client = MagicMock()
            mock_client.messages.create.return_value = Stream()
            with patch("app.backend.routes.response.Anthropic", return_value=mock_client):
                res = client.post("/api/response/stream", json={"prompt": "Say hi"})
                assert res.status_code == 200
                assert "data: a" in res.text
                assert "data: b" in res.text


def test_invalid_provider_returns_error(client):
    env = {
        "MODEL_PROVIDER": "invalid-provider",
        "MODEL_NAME": "test-model",
        "OPENAI_API_KEY": "openai-key",
        "ANTHROPIC_API_KEY": "anthropic-key",
    }

    with patch.dict(os.environ, env, clear=False):
        res = client.post("/api/response/generate", json={"prompt": "Say hi"})
        assert res.status_code in {400, 422, 500}
