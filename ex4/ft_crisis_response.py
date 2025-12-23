# ft_crisis_response.py
# Authorized: open(), read(), write(), with statement, try/except, print()

def crisis_handler(filename: str) -> None:
    print()
    # 危機シナリオっぽい見出し（例に合わせる）
    if filename == "standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'")

    print("...")

    try:
        # with により、成功/失敗に関わらず自動で close される
        with open(filename, "r") as f:
            data = f.read()

        # 成功ログ（例の雰囲気に合わせて表示）
        print(f"SUCCESS: Archive recovered - \"{data.strip()}\"")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        # 想定外のエラー（教材の「unexpected system anomalies」用）
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    # 生成ツールが作る想定の代表3パターン
    crisis_handler("lost_archive.txt")         # 存在しない
    crisis_handler("classified_vault.txt")     # 権限エラー想定
    crisis_handler("standard_archive.txt")     # 正常

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
