# SHARE-ALERTS

This app was created as part of a collection of time-limited code challenges, usually used as a way to explore different tech. It provides weekly updates on the performance of a share price chosen by the user.

## Roadmap

| Version | Update       | Feature                      | Completed |
| ------- | ------------ | ---------------------------- | --------- |
| v0.1.0  | Email        | Mid-week price snapshot      | ✅        |
| v0.2.0  | Email        | %/£ change in last week      | ✅        |
| v0.3.0  | Email        | %/£ change in last 28 days   | ✅        |
| v0.4.0  | Email        | %/£ change in last 6 month   | ✅        |
| v0.5.0  | Email        | %/£ change in last year      | ✅        |
| v0.6.0  | Email, Slack | implement slack notification | ✅        |
| v0.7.0  | Email, Slack | a nice graph                 |           |
| v0.8.0  | Email, Slack | User can choose stock        | ✅        |

## Dependencies

| Dependency                                             | Version |
| ------------------------------------------------------ | ------- |
| [Python](https://www.python.org/downloads/)            | 3.11.3  |
| [Poetry](https://python-poetry.org/docs/#installation) | 1.5.1   |

## Run locally

### Environment

Required variables:

```
EOD_API_KEY='< an eodhd api key >'
EOD_API_STOCK='< an eodhd api stock code >'
SEND_KEY_SECRET='< a unique key, identical to SEND_KEY, can be anything >'
SEND_KEY='< a unique key, identical to SEND_KEY_SECRET, can be anything >'
FROM_EMAIL='< a valid sendgrid account email >'
TO_EMAILS='< a comma+space separated list of emails, or a single email >'
SENDGRID_API_KEY='< a valid sendgrid api key >'
```

Optional variables:

```
WEBHOOK_URL='< a slack webhook url to send a table of stock data to a slack bot >'
```

### Running

```bash
make run
```

## Testing

For this repo we follow a user-generated e2e testing strategy. This involves releasing the software to users, at which point they perform e2e tests on the software for free! If they stop using the software, we know it needs to improve. Some of them might even tell us which specific bits are broken.
