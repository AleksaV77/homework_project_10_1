import pandas as pd


def list_financial_transactions_excel(df_file):
    """возвращает список словарей с данными о финансовых транзакциях из файла excel"""
    try:
        df = pd.read_excel(df_file)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        return f"файл {df_file} не найден"
    except Exception:
        return []


if __name__ == "__main__":
    file_excel = "C:/Users/asurk/PycharmProjects/Homework_Project1/data/transactions_excel.xlsx"
    print(list_financial_transactions_excel(file_excel))
