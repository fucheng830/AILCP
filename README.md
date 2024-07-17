# talu

## 项目介绍
一个AI agents，具备完整的管理后台，一键创建应用。
可以创建定时器任务，定时执行智能体。完全模拟人的行为，让智能体可以自动的执行任务，并且可以灵活的部署到不同的渠道。

初始邮箱：admin@example.com
初始密码：123456

## 项目特点

- 支持定时任务
- 支持创建应用
- 支持创建智能体
- 支持拖拽构建流程
- 支持部署到不同的渠道

## 项目演示

演示地址：https://aiagents.netlify.app/

## 项目截图

![image](https://user-images.githubusercontent.com/10094643/17368)

## 项目安装

## 项目功能

**用户模块:**

- 注册：
  - 邮件注册：用户通过提供邮箱地址和密码进行注册。注册成功后，系统将发送确认邮件到用户提供的邮箱，用户需要点击确认链接以完成注册流程。
  - 手机注册：用户通过提供手机号码和验证码进行注册。系统将向用户的手机发送验证码，用户需要输入正确的验证码来完成注册流程。
  - 第三方注册：用户可以选择使用第三方平台账号进行注册，如微信、谷歌、GitHub等。用户需要授权项目访问其第三方账号信息，以便创建新的账号或绑定现有账号。

- 登录：
  - 用户名密码登录：已注册用户使用注册时设置的用户名和密码进行登录。
  - 第三方登录：用户可以使用第三方平台账号进行登录，如微信、谷歌、GitHub等。用户需要授权项目访问其第三方账号信息，以完成登录流程。
  - 单点登录（SSO）：用户可以通过一次登录访问多个关联系统，允许用户在一个系统中进行认证后，在其他系统中无需重新登录。

- 插件：
  - 邮件发送插件：用于发送注册确认邮件、密码重置邮件等。通过集成邮箱服务提供商的 API，实现邮件的发送，包括自定义模板和内容等。
  - 手机短信发送插件：用于发送手机号验证码等短信通知。通过集成短信网关服务提供商的 API，实现短信的发送，包括验证码的生成和验证等。

- 用户个人资料管理：用户可以编辑和管理自己的个人信息，如昵称、头像、个人简介等。用户可以在个人资料页面进行信息的查看和编辑，并上传、更新头像等。

- 奖励和积分模块：
  - 积分系统：根据用户的活跃度、完成的任务等给予积分奖励。在系统中维护用户的积分账户，并根据定义的规则和条件对用户进行积分的增加、减少和查询。
  - 奖励规则管理：设定奖励的规则和条件，如积分兑换规则、等级制度等。定义不同的奖励规则，包括完成任务、推荐好友等，以激励用户的参与和活跃度。
  - 积分兑换：用户可以使用积分进行商品或服务的兑换。在商城或兑换平台中提供商品或服务的展示和交易，用户可以使用积分进行兑换，并处理相应的订单和物流流程。

**AI模块:**
- 工作流：为实现一系列复杂的任务或业务流程提供自动化解决方案。通过定义任务、任务依赖和工作流程，实现任务的顺序执行和自动化管理。
- 智能体：提供基于人工智能技术的智能对话和辅助功能，与用户进行自然语言交互，并提供相关的信息和服务。
- 插件：提供额外的功能和扩展模块，可根据需求进行自定义开发或集成第三方插件，以增强系统或应用的功能能力。
- 知识库：建立和维护一个集中存储和管理知识的库，包括文档、文章、FAQ等，用于提供信息检索和知识分享。

**计费系统:**
- 支付：实现用户支付功能，接收和处理用户的付款请求。集成支付网关或支付服务提供商的 API，支持各种支付方式，如信用卡支付、支付宝、微信支付等。
- 扣费：根据用户的服务使用情况，扣除相应的费用。根据定义的计费规则和费率，检测和计算用户的服务使用量，并进行费用扣除操作。
- 充值：用户可以通过充值渠道向账户充值资金，以便支付服务费用。支持充值渠道的接入和充值记录的管理，包括跟踪和验证充值操作。


## 扩展
支持以下渠道
- 微信
- 企业微信
- 微信公众号
- 网页
- 抖音
- 头条

## 工具
- 浏览器
- 搜索
- Http
- sendbox



