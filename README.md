# indie-site-playbook — B2B SaaS 独立站完整方法论

把 4 个独立站的踩坑经验，打包成了一套 AI 可直接执行的完整 Playbook。

从需求挖掘、建站、内容创作、联盟变现、Product Hunt 上线，到外链建设和长期运营，全流程覆盖，目标月收入 $2,000–$3,000。

---

## 这是什么

一套 Claude Code Skill，可以引导你（或你的 AI Agent）完成独立站建设的每一个阶段：

| 阶段 | 做什么 | 产出 |
|------|--------|------|
| 0 | 收益目标倒推，确定选题硬标准 | 筛选门槛 |
| 1 | 全平台调研 300–600 个候选方向 | 选题排名表 |
| 2 | 建站（Astro + Cloudflare Pages + monorepo） | 上线的网站 |
| 3 | 内容策略（Best X / Alternatives / vs / Review） | 20 篇文章 |
| 4 | 联盟计划接入与变现配置 | 联盟链接上线 |
| 5 | Product Hunt 上线 + SaaSHub + 目录提交 | 外链 + 流量 |
| 6 | 系统外链建设（免费 DR80–96 资源） | 域名权重提升 |
| 7 | 日常运营例程与规模化 | 收入持续增长 |

## 预期收益

- **第 3 个月**：网站上线，20 篇文章，第一笔联盟点击
- **第 6 个月**：月访问 5,000–8,000，月收入 $200–$500
- **第 12 个月**：月访问 15,000–22,000，月收入 $2,000–$3,000

## 适合谁

- 想做独立站副业的独立开发者和创作者
- 想系统化、数据驱动地进入 SaaS 联盟赛道的人
- 希望让 AI Agent 自主完成全流程执行的人

---

## 怎么用

### 方式一：Claude Code Skill

```bash
# 克隆仓库
git clone https://github.com/zhangwenhao66/indie-site-playbook.git

# 复制 skill 文件到 Claude 配置目录
cp indie-site-playbook/.claude/skills/indie-site-playbook.md ~/.claude/skills/
```

在 Claude Code 中调用：
```
/indie-site-playbook
```

AI 会询问你当前处于哪个阶段，然后从那里开始带你执行。

### 方式二：直接阅读

按顺序阅读 phases 目录下的文档：

1. `phases/00-goal-setting.md` — 收益目标设定
2. `phases/01-niche-research.md` — 选题调研完整 SOP
3. `phases/02-tech-stack-setup.md` — 建站技术栈
4. `phases/03-content-creation.md` — 内容创作策略
5. `phases/04-affiliate-monetization.md` — 联盟变现配置
6. `phases/05-launch-promotion.md` — 上线推广全攻略
7. `phases/06-backlink-building.md` — 外链建设体系
8. `phases/07-ongoing-operations.md` — 长期运营例程

---

## 技术栈（实际在用）

- **框架**：Astro 5.x
- **部署**：Cloudflare Pages（免费，500次构建/月）
- **结构**：pnpm monorepo（共享 UI + content-utils 包）
- **样式**：Tailwind CSS
- **数据分析**：Microsoft Clarity（免费热力图 + 录屏）
- **结构化数据**：JSON-LD（Organization / WebSite / Person）

## 用这套方法论建出来的站

| 网站 | 方向 | 状态 |
|------|------|------|
| tbc.com | HR & 薪资软件评测 | 上线中 |
| tbc.com | AP 自动化 & 报销软件 | 上线中 |
| tbc.com | 帮助台 & 客服工具 | 上线中 |
| tbc.com | 企业出海指南（中文） | 上线中 |

---

## License

MIT — 免费使用，欢迎 fork，去建你自己的站。
