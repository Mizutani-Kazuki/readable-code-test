def main():
    """
    同じフォルダにあるテキストファイルを読み込み、そのテキストに書いてある複数の言葉を出力する
    """
    with open("words_list2.txt", "r", encoding="utf-8") as f:
        words = [word.strip() for word in f.readlines()]
    for idx, word in enumerate(words):
        print(f"{idx+1}: {word}")
    

if __name__ == "__main__":
    main()