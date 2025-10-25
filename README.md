# API自动化测试项目

基于 pytest + allure 的 API 接口自动化测试框架

## 项目结构

```
pt1021/
├── .github/
│   └── workflows/
│       └── test.yml          # GitHub Actions CI/CD配置
├── data/                      # 测试数据目录
│   └── login_data.yaml       # 登录测试数据
├── tests/                     # 测试用例目录
│   ├── conftest.py           # pytest配置文件
│   └── test_login.py         # 登录接口测试
├── utils/                     # 工具类目录
│   └── api_request.py        # API请求封装
└── requirements.txt           # 项目依赖
```

## 环境要求

- Python 3.8+
- pytest >= 8.0.0
- allure-pytest >= 2.13.0

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行测试

### 基本运行
```bash
pytest tests/
```

### 生成Allure报告
```bash
# 运行测试并生成allure数据
pytest tests/ --alluredir=allure-results

# 查看报告
allure serve allure-results
```

## 功能特性

✅ pytest测试框架  
✅ 参数化测试  
✅ YAML数据驱动  
✅ Allure测试报告  
✅ API请求封装  
✅ Fixture复用  
✅ GitHub Actions CI/CD自动化  
✅ 自动部署测试报告到GitHub Pages  

## CI/CD

项目已配置GitHub Actions自动化流程：
- 推送到main/develop分支时自动运行测试
- 自动生成Allure测试报告
- 报告自动部署到GitHub Pages

查看测试报告：`https://u1219437219-cmyk.github.io/pytest_api1025/report/`

## 测试用例说明

### 登录接口测试 (test_login.py)
- ✅ 正确的用户名密码登录成功
- ✅ 错误的密码登录失败

## 后续计划

- [ ] 集成真实的HTTP请求
- [ ] 添加更多接口测试用例
- [ ] 完善错误处理机制
- [ ] 数据库断言支持

## License

MIT
