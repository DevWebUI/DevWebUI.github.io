# DevWebUI: pricing

Machine-readable pricing summary for agentic buyers and comparison engines.

```yaml
product: DevWebUI
vendor: LunarWerx Studios
homepage: https://devwebui.lunarwerx.com/
repository: https://github.com/LunarWerxs/devwebui
license: MIT
price: 0
currency: USD
billing_model: none
account_required: false
cloud_required: false
open_source: true
version: 0.8.7
```

## Summary

DevWebUI is free. It is open source under the MIT License: copy it, modify it, self-host it,
or redistribute it, with no royalty and no attribution requirement beyond the license text
itself. There is no paid tier, no subscription, no seat count, no usage cap, and no feature
gated behind payment. You run it entirely on your own machine.

## What you get for $0

- The full GUI: one-click start/stop/restart, live status, CPU, memory and log view for every
  process it manages.
- The full MCP server (31 tools) for AI agents to drive the same daemon.
- The CLI, the Windows tray app, the prebuilt Windows installer, and the source.
- Every feature on the roadmap ships free too; there is no "pro" edition planned.

## Optional extras (both free, both off by default)

| Extra | Cost | Requires an account? | Default |
|---|---|---|---|
| Settings sync (preferences/theme across machines) | $0 | Yes, a LunarWerx Connections account | Off |
| Anonymous install ping (update-check counter) | $0 | No | On (silently fails if offline; disable with `DEVWEBUI_NO_PING=1`) |

Neither extra unlocks a feature the free product lacks; sync just carries your prefs between
machines, and the ping is only a coarse install counter used for update checks.

## Costs you bear yourself (bring-your-own)

None. DevWebUI does not call any paid third-party API, does not require a database service,
and does not meter usage against an external provider. It is a local daemon; the only
"infrastructure" is the machine you already run your dev servers on.

## Comparison note

DevWebUI is free end-to-end, including its GUI and its MCP server. For contrast: PM2's own
web dashboard, PM2 Plus, is a paid add-on over PM2's free CLI, with plans starting around
$39/month (source: https://pm2.io/pricing). hotel and exo, the other two process managers
people commonly compare DevWebUI against, are free.

## Links

- Full brief: https://devwebui.lunarwerx.com/llms-full.txt
- License text: https://github.com/LunarWerxs/devwebui/blob/main/LICENSE
- Source: https://github.com/LunarWerxs/devwebui
