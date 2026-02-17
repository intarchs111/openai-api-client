
# OpenAI API Client Demo 

![Architecture](https://img.shields.io/badge/Pattern-OpenAI%20Integration-blue)
[![openai-api-client](https://img.shields.io/badge/Github-openai--api--client-purple?style=flat-square&logo=github)](https://github.com/intarchs111/openai-api-client)
![Python](https://img.shields.io/badge/python-3.10+-blue)

***Created by: [Suyog Hire - Solutions Architect](https://linkedin.com/in/suyoghire)***

---

A simple demonstration of the OpenAI API's Responses endpoint, showcasing how to make API calls and retrieve model outputs using Python.

## Features

- Environment-based API key management for security
- Simple implementation of OpenAI's Responses API
- Demonstrates the `gpt-5-nano` model usage
- Clean, well-documented code structure

## Prerequisites

Before running this project, ensure you have:

- Python 3.10 or higher
- An OpenAI API account and API key ([sign up here](https://platform.openai.com/signup))
- pip (Python package manager)

## Installation

[![openai-api-client](https://img.shields.io/badge/Github-openai--api--client-purple?style=flat&logo=github)](https://github.com/intarchs111/openai-api-client)

1. **Clone the repository**

```bash
  git clone https://github.com/intarchs111/openai-api-client.git
  cd openai-api-client
```

2. **Install required dependencies**

Install dependencies
- 'openai' - Official OpenAI Python library
- 'python-dotenv' - Environment variable management

```bash
  pip install openai python-dotenv
```

3. **Set up your environment variables**

Create a '.env' file in the project root directory:
Add your OpenAI API key to the '.env' file:

**Important**: Never commit your '.env' file to version control. Add it to your '.gitignore' file.

   
## Configuration

You can modify the following parameters in `openai-api-client-ss.py`:

| Parameter | Description | Default Value |
|-----------|-------------|---------------|
| `model` | The OpenAI model to use | `gpt-5-nano` |
| `input` | The prompt/question to send | `"What is the capital of France?"` |
| `max_output_tokens` | Maximum tokens in the response | `300` |
| `store` | Whether to store the request/response | `False` |

## Usage/Examples

Run the script from the command line:

The script will:
1. Load your API key from the '.env' file
2. Initialize the OpenAI client
3. Send a request to the Responses API with the input: "What is the capital of France?"
4. Print the model's response

```bash
  python openai-api-client-ss.py
```
## Security Best Practices

- Store API keys in environment variables, never hardcode them 
- Use `.env` files for local development 
- Add `.env` to your `.gitignore` file
- Consider using secret management tools for production environments

## Not in Scope

This project intentionally focuses on a minimal, self-contained demonstration of the OpenAI Responses API. The following are deliberately excluded to keep the example simple and focused:

*   **Production-grade error handling** (e.g., retries, rate limiting, API downtime recovery).
*   **Advanced authentication** (e.g., OAuth, service accounts, or multi-key rotation).
*   **Response storage/retrieval** when store=True (demo uses store=False).
*   **Logging, monitoring, or observability** integrations.
*   **Web UI, CLI interface, or input validation** for user prompts.
*   **Testing suite** (unit tests, integration tests).
*   **Containerization** (Docker) or deployment configurations (CI/CD, cloud providers).
*   **Multi-model support** or dynamic model selection.
*   **Cost tracking** or usage analytics.

## Troubleshooting

**Issue**: `ModuleNotFoundError: No module named 'openai'`
- **Solution**: Run `pip install openai python-dotenv`

**Issue**: `AuthenticationError: Invalid API key`
- **Solution**: Verify your API key in the `.env` file is correct and active

**Issue**: API response errors
- **Solution**: Check the [OpenAI API status page](https://status.openai.com/) and verify your account has available credits


## Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [OpenAI Python Library](https://github.com/openai/openai-python)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) - More examples and guides

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Repository
**OpenAI Responses API Client**   

[![openai-api-client](https://img.shields.io/badge/Github-openai--api--client-purple?style=flat-square&logo=github)](https://github.com/intarchs111/openai-api-client)

## Acknowledgments

This project utilizes established open-source libraries and official documentation to enable secure and efficient OpenAI API integration.
​
- **OpenAI Python SDK** – The official library for interacting with OpenAI APIs.
- **​OpenAI API Reference** – Comprehensive documentation for the Responses API endpoint.
- **​python-dotenv** – For loading environment variables from .env files securely.

---

<div align="center">


### **Suyog Hire** | **AI Solutions Architect**
[![github-profile](https://img.shields.io/badge/GitHub-grey?style=flat&logo=github)](https://github.com/intarchs111) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/suyoghire)

</div>
