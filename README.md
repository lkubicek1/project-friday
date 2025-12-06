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

### 3\. Local Development Setup

To run F.R.I.D.A.Y. on your own machine for testing, follow these steps:

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Configure Environment Variables

Create a `.env` file in the project root with your credentials:

```ini
GEMINI_API_KEY=AIzaSy...
DISCORD_TOKEN=MTAxy...
DISCORD_CHANNEL_SPACE=123456789...
DISCORD_CHANNEL_FINANCE=123456789...
```

> **Note:** No quotes are needed around values in a `.env` file.

#### Verify `.gitignore`

**Important:** Ensure `.env` is listed in your `.gitignore` to prevent accidentally committing secrets:

```text
.env
```

#### Run a Test Report

With your `.env` file in place, run:

```bash
python src/friday_core.py --report_id morning_space_brief
```

The script automatically loads environment variables from `.env` using `python-dotenv`. When deployed, GitHub Actions ignores the `.env` file and uses Repository Secrets instead.

### 4\. Deploy

Simply push to your main branch. The GitHub Actions defined in `.github/workflows/` will automatically register the schedules.

```bash
git add .
git commit -m "Initialize F.R.I.D.A.Y. Protocol"
git push origin main
```

-----

## 🔑 External Service Setup

F.R.I.D.A.Y. requires two external services: **Google Gemini** for AI-powered analysis and **Discord** for delivering reports. Follow these guides to set up each service from scratch.

### Google Gemini API Setup

#### 1. Create a Google Account (if needed)

If you don't have a Google account, create one at [accounts.google.com](https://accounts.google.com).

#### 2. Access Google AI Studio

1. Navigate to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Accept the Terms of Service when prompted

#### 3. Create a Project (Optional but Recommended)

While AI Studio can work without a dedicated project, creating one helps organize your usage:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click the project dropdown at the top of the page
3. Click **New Project**
4. Name it something like `project-friday` and click **Create**
5. Select your new project from the dropdown

#### 4. Generate an API Key

1. Return to [Google AI Studio](https://aistudio.google.com/)
2. Click **Get API Key** in the left sidebar
3. Click **Create API Key**
4. If prompted, select your project (or use the default)
5. Copy the generated key immediately — it won't be shown again

> **Security:** Treat this key like a password. Never commit it to version control or share it publicly.

#### 5. Verify Your Key

Test that your key works:

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models?key=YOUR_API_KEY"
```

You should see a JSON response listing available models.

---

### Discord Bot Setup

#### 1. Create a Discord Server (if needed)

If you don't have a server for F.R.I.D.A.Y.:

1. Open Discord (desktop or web)
2. Click the **+** button in the server list (left sidebar)
3. Select **Create My Own**
4. Choose **For me and my friends** (or your preference)
5. Name your server and click **Create**

#### 2. Create a Discord Application

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application** (top right)
3. Name it `F.R.I.D.A.Y.` (or your preference) and click **Create**
4. Optionally, add a description and app icon on the General Information page

#### 3. Create the Bot

1. In your application, click **Bot** in the left sidebar
2. Click **Reset Token** (or **Add Bot** if it's a new application)
3. Confirm by clicking **Yes, do it!**
4. Click **Copy** to copy your bot token — save this securely

> **Security:** This token grants full control of your bot. Never share it or commit it to version control.

#### 4. Configure Bot Permissions

Still on the Bot page:

1. Scroll down to **Privileged Gateway Intents**
2. Enable **Message Content Intent** (required for reading/sending messages)
3. Click **Save Changes**

#### 5. Invite the Bot to Your Server

1. Click **OAuth2** in the left sidebar, then **URL Generator**
2. Under **Scopes**, select:
   - `bot`
3. Under **Bot Permissions**, select:
   - `Send Messages`
   - `Embed Links` (for rich message formatting)
4. Copy the generated URL at the bottom
5. Paste it into your browser
6. Select your server from the dropdown and click **Authorize**

#### 6. Get Channel IDs

F.R.I.D.A.Y. needs the numeric ID of each channel it should post to:

1. In Discord, go to **User Settings** (gear icon)
2. Navigate to **App Settings** > **Advanced**
3. Enable **Developer Mode**
4. Return to your server
5. Right-click the channel (e.g., `#space-news`) and select **Copy Channel ID**
6. Repeat for each channel you want F.R.I.D.A.Y. to use

#### 7. Create Your Channels

Create dedicated channels for each report type:

1. Right-click your server name > **Create Channel**
2. Create text channels like:
   - `#space-news` — for the morning space brief
   - `#market-watch` — for the market opening report
3. Copy each channel's ID as described above

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
