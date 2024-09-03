# 🔥 Warm - Keep Your APIs Cozy

<p align="center">
  <img src="https://img.shields.io/badge/python-3.7%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/github/licenseYoussefbaghr/Warm" alt="License">
  <img src="https://img.shields.io/github/starsYoussefbaghr/Warm" alt="Stars">
  <img src="https://img.shields.io/github/forksYoussefbaghr/Warm" alt="Forks">
</p>

Warm is a robust, asynchronous API warming tool designed to keep your services active and responsive. Perfect for preventing cold starts on platforms like Render, Heroku, and more.

## 🌟 Features

-   🚀 **Asynchronous Pinging**: Efficiently warm multiple APIs concurrently
-   ⏱️ **Flexible Scheduling**: Customize ping intervals to suit your needs
-   🔧 **Easy Configuration**: Simple setup using environment variables
-   📊 **Detailed Logging**: Comprehensive logs for monitoring and debugging
-   🔁 **Automatic Retries**: Built-in mechanism to handle temporary failures
-   🧪 **Test Coverage**: Ensure reliability with our test suite

## 🚀 Quick Start

1. **Clone and install:**

    ```bash
    git clone https://github.comYoussefbaghr/Warm.git
    cd warm
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

2. **Configure:**

    Copy `.env.example` to `.env` and adjust the values:

    ```env
    API_URL_1=https://your-api-1.com
    API_URL_2=https://your-api-2.com
    PING_INTERVAL=60  # minutes
    ```

3. **Run:**

    ```bash
    python main.py
    ```

## 📊 Monitoring

View real-time logs:

```bash
tail -f warm.log
```

## 🧪 Testing

Run the test suite:

```bash
pytest
```

## 📖 Documentation

-   [Usage Guide](docs/USAGE.md)
-   [Contribution Guidelines](docs/CONTRIBUTING.md)
-   [Changelog](docs/CHANGELOG.md)

## 🤝 Contributing

Contributions are welcome! Please check out our [Contribution Guidelines](docs/CONTRIBUTING.md).

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

Having issues or questions? [Open an issue](https://github.com/Youssefbaghr/Warm/issues) on GitHub.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/Youssefbaghr">Your Name</a>
</p>

<p align="center">
  <a href="https://github.com/Youssefbaghr/Warm/stargazers">Star this project</a> •
  <a href="https://github.com/Youssefbaghr/Warm/issues">Report an issue</a>
</p>

Stay warm! 🔥
