# Project F.R.I.D.A.Y. 🤖

![License](https://img.shields.io/badge/license-MIT-green) ![Python](https://img.shields.io/badge/python-3.9-blue) ![Status](https://img.shields.io/badge/status-active-success)

> **A serverless, AI-driven intelligence system for Discord.**

F.R.I.D.A.Y. is an automated agent that "wakes up" on a schedule, scours the web for high-value intelligence, and delivers concise briefings to your channels. Powered by **Google Gemini** and **GitHub Actions**, it runs entirely in the cloud.

---

## 📡 Active Protocols

### 🚀 Space Command (Morning Brief)
* **Schedule:** Daily @ 08:00 UTC
* **Objective:** Global situational awareness on exploration and regulation.
* **Intel Sources:** * Pre-print Research (`site:arxiv.org`)
    * Launch Manifests (`site:spacenews.com`)
    * Legal Filings (`site:courtlistener.com`)

### 📈 Market Watch (Opening Bell)
* **Schedule:** Mon-Fri @ 13:15 UTC (Pre-Market)
* **Objective:** Identify volatility and key economic drivers before the bell.
* **Intel Sources:**
    * Pre-market movers (Bloomberg/CNBC)
    * Federal Reserve Calendar
    * Global Macroeconomic Data

---

## 🛠️ Architecture

F.R.I.D.A.Y. operates on a **Data-Driven** architecture. Logic is separated from configuration, meaning you can tweak prompts or add new reports just by editing a YAML file, without touching the Python code.

```mermaid
graph LR
    A[GitHub Schedule] -->|Triggers| B(Python Engine)
    B -->|Reads Config| C{reports.yaml}
    B -->|Queries| D[Gemini API]
    D -->|Google Search| E[Live Web Data]
    D -->|Summarizes| B
    B -->|Transmits| F[Discord Channel]
````

-----

## ⚡ Quick Start

### 1\. Fork & Clone

```bash
git clone [https://github.com/lkubicek1/project-friday.git](https://github.com/lkubicek1/project-friday.git)
cd project-friday
```

### 2\. Configure Secrets

F.R.I.D.A.Y. needs credentials to operate. Go to your GitHub Repo:
`Settings` \> `Secrets and variables` \> `Actions` \> `New repository secret`

| Secret Key | Description |
| :--- | :--- |
| `GEMINI_API_KEY` | Get this from [Google AI Studio](https://aistudio.google.com/). |
| `DISCORD_TOKEN` | Your Bot Token from the [Discord Developer Portal](https://discord.com/developers/applications). |
| `DISCORD_CHANNEL_SPACE` | Right-click your **\#space-news** channel and "Copy ID". |
| `DISCORD_CHANNEL_FINANCE` | Right-click your **\#market-watch** channel and "Copy ID". |

### 3\. Install Dependencies (Local Testing)

If you want to run it on your own machine to test:

```bash
pip install -r requirements.txt
# You must export your API keys as environment variables first!
python src/friday_core.py --report_id morning_space_brief
```

### 4\. Deploy

Simply push to your main branch. The GitHub Actions defined in `.github/workflows/` will automatically register the schedules.

```bash
git add .
git commit -m "Initialize F.R.I.D.A.Y. Protocol"
git push origin main
```

-----

## ⚙️ Customization

To modify the personality or search targets, edit `config/reports.yaml`:

```yaml
# Example Entry
market_open:
  display_name: "📈 F.R.I.D.A.Y. | Market Watch"
  channel_env_var: "DISCORD_CHANNEL_FINANCE"
  prompt_template: |
    Today is {date}. Search for top gainers...
```

To change the schedule, edit the cron timer in `.github/workflows/schedule_market.yml`.

-----

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
```
