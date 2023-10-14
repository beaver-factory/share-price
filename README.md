# SHARE-ALERTS

This app provides weekly updates on the performance of the [Northcoders Groups PLC (CODE)](https://www.londonstockexchange.com/stock/CODE/northcoders-group-plc/company-page) share price.

## Roadmap

| Version | Update       | Feature                      | Completed |
| ------- | ------------ | ---------------------------- | --------- |
| v0.1.0  | Email        | Mid-week price snapshot      | ✅        |
| v0.2.0  | Email        | %/£ change in last week      | ✅        |
| v0.3.0  | Email        | %/£ change in last 28 days   | ✅        |
| v0.4.0  | Email        | %/£ change in last 6 month   | ✅        |
| v0.5.0  | Email        | %/£ change in last year      | ✅        |
| v0.6.0  | Email, Slack | implement slack notification |           |
| v0.7.0  | Email, Slack | a nice graph                 |           |
| v0.8.0  | Email, Slack | User can choose stock        |           |

## Dependencies

| Dependency                                             | Version |
| ------------------------------------------------------ | ------- |
| [Python](https://www.python.org/downloads/)            | 3.11.3  |
| [Poetry](https://python-poetry.org/docs/#installation) | 1.5.1   |

## Run locally

```bash
make run
```

## Architecture

Keep it simple. A single github workflow can be used to [schedule](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule) the weekly cron.

Then you _just_ need to write some code that gets all the data required for the features.

## Testing

For this repo we follow a user-generated e2e testing strategy. This involves releasing the software to users, at which point they perform e2e tests on the software for free! If they stop using the software, we know it needs to improve. Some of them might even tell us which specific bits are broken.
