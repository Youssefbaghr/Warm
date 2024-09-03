# 🔥 Warm - Keep Your APIs Cozy

<p align="center">
  <img src="https://img.shields.io/badge/python-3.7%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
  <a href="https://github.com/Youssefbaghr/warm/actions"><img src="https://github.com/Youssefbaghr/warm/workflows/tests/badge.svg" alt="Tests"></a>
</p>

Warm is a robust, asynchronous API warming tool designed to keep your services active and responsive. Perfect for preventing cold starts on platforms like Render, Heroku, and more.

## 🌟 Features

-   🚀 **Asynchronous Pinging**: Efficiently warm multiple APIs concurrently
-   ⏱️ **Flexible Scheduling**: Customizable run intervals and ping frequencies
-   🔧 **Easy Configuration**: Simple setup using environment variables
-   📊 **Detailed Logging**: Comprehensive logs for monitoring and debugging
-   🔁 **Automatic Retries**: Built-in mechanism to handle temporary failures
-   🎨 **Colorful Console Output**: Visually appealing and easy-to-read logs

## 🚀 Quick Start

1. **Clone and install:**

    ```bash
    git clone https://github.com/Youssefbaghr/Warm.git
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
    RUN_INTERVAL=720
    PING_INTERVAL=60
    LOG_LEVEL=INFO
    LOG_FILE=warm.log
    ```

    - `API_URL_x`: Add as many API URLs as you need, incrementing the number for each new URL.
    - `RUN_INTERVAL`: The interval between service runs in minutes (default is 720, which is 12 hours).
    - `PING_INTERVAL`: The interval between pings within a run in minutes (default is 60).
    - `LOG_LEVEL`: Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    - `LOG_FILE`: The name of the log file (default is warm.log).

3. **Run:**

    ```bash
    python main.py
    ```

## 📊 Monitoring

You can monitor Warm's activity in two ways:

1. Console output: Warm will print log messages to the console as it runs.
2. Log file: Check the log file (default: `warm.log`) for detailed information:

    ```bash
    tail -f warm.log
    ```

## 🧪 Testing

Run the test suite:

```bash
pytest
```

## 🛠 Customization

To modify Warm's behavior:

1. Edit `src/ping.py` to change how APIs are pinged.
2. Modify `src/scheduler.py` to adjust scheduling logic.
3. Update `src/config.py` to add new configuration options.

## 🚀 Deployment

To deploy Warm:

1. Choose a hosting platform (e.g., Heroku, DigitalOcean, AWS).
2. Set up environment variables on your chosen platform.
3. Deploy the code following the platform's specific instructions.
4. Ensure the service is configured to run continuously.

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

Please ensure your code passes all tests and follows the project's coding style.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

Having issues or questions? [Open an issue](https://github.com/Youssefbaghr/Warm/issues) on GitHub.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/Youssefbaghr">Youssef Baghrous</a>
</p>

<p align="center">
  <a href="https://github.com/Youssefbaghr/Warm/stargazers">Star this project</a> •
  <a href="https://github.com/Youssefbaghr/Warm/issues">Report an issue</a>
</p>

Stay warm! 🔥
