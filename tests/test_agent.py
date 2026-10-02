from app.agent import build_answer


def test_agent_answers_supported_request() -> None:
    result = build_answer("Как запустить проект?")

    assert result["status"] == "ok"
    assert "README" in result["answer"]


def test_agent_rejects_empty_message() -> None:
    result = build_answer("   ")

    assert result["status"] == "error"
    assert "Опишите задачу" in result["answer"]


def test_agent_requests_context_for_unknown_topic() -> None:
    result = build_answer("Какая сегодня погода?")

    assert result["status"] == "needs_clarification"
    assert "Уточните контекст" in result["answer"]


def test_response_contract_is_stable() -> None:
    result = build_answer("Нужна инструкция")

    assert set(result) == {"status", "answer"}
