# AGENTS.md

課程倉庫（`115-1 計算機程式`）。目前僅有 `README.md` + Python `.gitignore`，尚無 source、build、test、lint 設定。

- 所有的回應都使用繁體中文。
- 專案所使用的程式語言為 Python。
- 使用 conda 管理 Python 套件，環境名稱為 `iem_python`。
  - 執行程式：`conda run -n iem_python python <script>.py`
  - 安裝套件：`conda install -n iem_python <pkg>`（非 conda 提供的才用 `conda run -n iem_python pip install <pkg>`）
- 尚無測試框架與 CI，新增程式碼請以實際執行驗證。
- 新增檔案預設放在 repo 根目錄；未經要求不要自創 pyproject/requirements/CI 等工具設定。
