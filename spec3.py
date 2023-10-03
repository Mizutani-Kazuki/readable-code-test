def main():
    """
    同じフォルダにあるテキストファイルを読み込み、そのテキストに書いてある言葉を出力する
    """
    with open("words_list.txt", "r", encoding="utf-8") as f:
        word = f.read()
    print(word)
    

if __name__ == "__main__":
    main()