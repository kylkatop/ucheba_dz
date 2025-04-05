from datetime import datetime
from typing import List

from src.masks import mask_account_number, mask_card_number


def mask_account_card(account_info: str) -> str:
    """
    Скрывает данные о карте или счете.

    :param account_info: Строка в формате 'Visa Platinum 7000792289606361' или 'Счет 73654108430135874305'
    :return: Строка с замаскированными данными
    """
    # Разделяем строку на части, разделенные пробелами
    parts = account_info.split()
    if len(parts) < 2:
        raise ValueError("Неверный формат входных данных")

    if parts[0].lower() == "счет":
        if len(parts) != 2:
            raise ValueError("Неверный формат счета")
        return f"{parts[0]} {mask_account_number(parts[1])}"
    else:
        card_name = " ".join(parts[:-1])
        card_number = parts[-1]
        return f"{card_name} {mask_card_number(card_number)}"


def get_date(date_str: str) -> str:
    """
    Конвертирует дату из формата ISO 8601 в формат ДД.ММ.ГГГГ.

    :param date_str: Строка с датой в формате '2024-03-11T02:26:18.671407'
    :return: Дата в формате '11.03.2024'
    """
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Неверный формат даты")