import pandas as pd


def list_financial_transactions_csv(df_file):
    """возвращает список словарей с данными о финансовых транзакциях из файла csv"""
    try:
        with open(df_file, encoding="utf-8") as file:
            df = pd.read_csv(file, delimiter=";")
            return df.to_dict(orient="records")
    except FileNotFoundError:
        return f"файл {df_file} не найден"
    except Exception:
        return []


if __name__ == "__main__":
    file_csv = "C:/Users/asurk/PycharmProjects/Homework_Project1/data/transactions.csv"
    print(list_financial_transactions_csv(file_csv))
