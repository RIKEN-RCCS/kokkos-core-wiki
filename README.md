# Kokkos　コア文書ウェブサイト
Kokkos ドキュメンテーションレポジトリにようこそ。  これは、 https://kokkos.github.io/kokkos-core-wiki/.のソースです。

## ローカル環境で　HTML ページを作成するための要件

ドキュメントのビルドには最低でも Python 3.12 が必要です。通常はシステムのパッケージマネージャーでインストールできますが、お使いのシステムが Python 3.12 以上をサポートしていない場合は、[pyenv](https://github.com/pyenv/pyenv)を使って簡単にインストールできます。
これはドキュメントのローカルレンダリング専用に必要なもので、プッシュ前に確認できるようになります。
要件は、 `build_requirements.txt`にあります。
以下を使って、インストール可能です: `pip install -r build_requirements.txt`

仮想環境の使用を推奨します。例えば、システムの Python が 3.12 以上の場合は次のようにします:

```sh
python -m venv venv
source venv/bin/activate
pip install -r build_requirements.txt
```

pyenv を使用している場合は次のようにします:

```sh
pyenv install 3.12
pyenv shell 3.12
python -m venv venv
pyenv shell --unset
source venv/bin/activate
pip install -r build_requirements.txt
```

## ビルド

```
cd docs
make html
```

クリーンのため:
```
cd docs
make clean
```

## サイトをローカルで表示

ウェブブラウザで、`docs/generated_docs/index.html` を開くことが可能で、または、その代わりに、python　に組み込まれた  http サーバーを使用できます:

```bash
cd docs/generated_docs
python3 -m http.server
```

次に、 http://localhost:8000
に移動してください。

その代わりに、あるいは、make　を実行するたびに自動更新を希望する場合は、[httpwatcher](https://pypi.org/project/httpwatcher/) と組み合わせて、ドキュメンテーションを利用できます。
