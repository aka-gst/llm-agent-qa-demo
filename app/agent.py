"""Deterministic agent logic used for reproducible QA scenarios."""

SUPPORTED_TOPICS = ("запуск", "проект", "инструкция", "тест")


def build_answer(message: str) -> dict[str, str]:
    """Return a predictable answer suitable for automated QA checks."""
    normalized = message.strip()
    if not normalized:
        return {
            "status": "error",
            "answer": "Опишите задачу или задайте вопрос, чтобы я мог помочь.",
        }

    if any(topic in normalized.lower() for topic in SUPPORTED_TOPICS):
        return {
            "status": "ok",
            "answer": "Начните с README: установите зависимости, настройте окружение и запустите тесты.",
        }

    return {
        "status": "needs_clarification",
        "answer": "Уточните контекст задачи: проект, запуск, инструкция или тестирование.",
    }
