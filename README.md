# console_translator

🖥️ **console_translator** は、英語で表示されるコンソール出力・エラーコード・ログメッセージを  
**自動で日本語に翻訳する Python ライブラリ**です。

「pip のエラーが英語で読めない」  
「download / install のログが何言ってるかわからん」  
そんな人のために作られました。

---

## 🔥 特徴

- ✅ **英語のコンソール出力を日本語に翻訳**
- ✅ `print` などの **Python構文・関数名は翻訳しない**
- ✅ `download`, `install`, `error` などの **メッセージだけ翻訳**
- ✅ pip / Python / Linux / Colab 対応
- ✅ 学習用途・初心者・英語が苦手な人向け

---

## 🧠 仕組み（ざっくり）

- 出力テキストを解析
- **コード・関数名・予約語を除外**
- 人間が読む部分（エラー文・説明文）だけ翻訳
- コンソールに日本語で再表示

---

## 📦 インストール方法

### GitHub から直接インストール（推奨）

```bash
pip install git+https://github.com/Ryouse1/console_translator.git

##Google Colab の場合
!pip install git+https://github.com/Ryouse1/console_translator.git
