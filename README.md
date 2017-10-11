# XOJ需求规格说明书

<img src="images/logo.png" width="30%">

#### 文档摘要

|  项目名称  |   XOJ代码评测分析平台   |
| :----: | :-------------: |
|  文档名称  | XOJ-Req-需求规格说明书 |
|  责任人   |       徐恒达       |
| 最后修改时间 |    2017.10.9    |
|  最新版本  |      v2.0       |

#### 版本更新摘要

| 版本号  |   更新时间    | 更新者  |    更新摘要    |
| :--: | :-------: | :--: | :--------: |
| v0.1 | 2017.9.30 | 徐恒达  |  确定文档基本框架  |
| v0.2 | 2017.10.2 | 王志伟  |   完善引言部分   |
| v0.9 | 2017.10.5 | 夏计强  |  完善项目概述部分  |
| v1.0 | 2017.10.6 | 扎西顿珠 |  修改部分术语解释  |
| v1.2 | 2017.10.7 | 徐博航  |  完善其他需求部分  |
| v2.0 | 2017.10.9 | 徐恒达  | 对功能需求进一步细化 |
|      |           |      |            |

​      

# 目录      

[TOC]

​     

​     

## 1. 引言

### 1.1 编写目的

编写 XOJ在线测试平台需求分析报告目的是为了明确开发目的。经确认后，将作为开发方设计开发的基本依据和需求方的软件验收标准，同时，通过该需求分析报告，开发方可以进一步了解客户的需求，从而严格按照流程及时、准确地完成系统的开发，以满足客户的需求。同时，该文档也作为概要设计及后续设计的基础。

### 1.2 范围

- 适用于高校学生程序设计的训练、参赛队员的训练和选拔、各种程序设计竞赛以及数据结构和算法的学习和作业的自动提交判断。
- 适用于市面上所有主流浏览器。

### 1.3 术语与缩写解释

#### 1.3.1 通用术语

- Online Judge：在线评测网站Online Judge，简称OJ，是一个在线判题系统，系统中收录了大量不同类型的算法编程题，用户可以提交自己的代码，系统会对用户提交的源代码进行编译，运行。对于每道题，系统中存有大量的预置输入输出数据，通过对比用户代码生成的程序产生的输出与预置的输出返回给用户不同的结果。


- POJ：北京大学的在线评测系统.题目数量很多,OJ的各项功能也很完善,而且还提供免费的OJ系统下载，可以利用提供的系统自己搭建OJ.题目数量很多,有几千道,但水题也很多.关于这一点,因为题目数量大,所以水题自然就多,但这不说明POJ的题目质量不高.POJ的难题还是不少的,而且做不做水题还是要由做题人自己决定的,和OJ无关。


#### 1.3.2 评测平台返回状态缩写

- Queuing : 提交太多了，OJ无法在第一时间给所有提交以评判结果，后面提交的程序将暂时处于排队状态等待OJ的评判。不过这个过程一般不会很长。
- Compiling : 您提交的代码正在被编译。
- Running : 您的程序正在OJ上运行。
- Judging : OJ正在检查您程序的输出是否正确。
- Accepted (AC) : 您的程序是正确的，恭喜！
- Presentation Error (PE) : 虽然您的程序貌似输出了正确的结果，但是这个结果的格式有点问题。请检查程序的输出是否多了或者少了空格（' '）、制表符（'\t'）或者换行符（'\n'）。
- Wrong Answer (WA) : 输出结果错，表示该程序一个或多个用例错误
- Runtime Error (RE) : 运行时错误，这个一般是程序在运行期间执行了非法的操作造成的。以下列出常见的错误类型：


- Time Limit Exceeded (TLE) : 您的程序运行的时间已经超出了这个题目的时间限制。
- Memory Limit Exceeded (MLE) : 您的程序运行的内存已经超出了这个题目的内存限制。
- Compilation Error (CE) : 您的程序语法有问题，编译器无法编译。具体的出错信息可以点击链接察看。

### 1.4 参考文献

- 计算机软件需求规格说明规范GB/T 9385—2008（Norm of computer software requirements specification）
- Online Judge - 百度百科 https:// baike.baidu.com/item/Online%20Judge/2397914?fr=aladdin

## 2. 项目概述

### 2.1 项目背景

在学习编程技术的过程中，越来越多的小伙伴喜欢拿一些OJ平台的编程题练手。OJ，即Online Judge（在线评测网站），收录了大量不同类型的算法编程题，用户可以提交自己的代码，系统会对用户提交的源代码进行 编译，运行。对于每道题，系统中存有大量的预置输入输出数据，通过对比用户代码生成的程序产生的输出与预置的输出返回给用户不同的结果。国内外有许多非常著名的，收录题目非常全的OJ系统。 

在做各OJ平台编程练习时，用户常常找不到合适的算法解决问题，苦于在百度、谷歌上搜寻各种相关的代码资料学习，并一遍遍的调试，十分麻烦。

本项目旨在帮助用户解决棘手的编程题，实现在互联网上快速搜索题目相关代码，并传输回OJ平台进行评测，将可用代码返回给用户。同时加入用户编程学习进程分析，让用户对自己的编程水平有一个更清晰的了解。

### 2.2 需求概述

实现一个针对OJ网站的“作弊”平台，该平台利用爬虫技术，将用户所提交申请的OJ平台网页上题目相关信息记录下来，然后在互联网上搜取相关代码并进行评测，最后返回评测通过的代码，从而帮助用户解决一些棘手的编程题目。同时，该平台对用户的提交及评测结果历史进行记录和分析，让用户对自己的学习情况有更全面的了解。

### 2.3 用户特点

本项目的目标用户人群主要为

1. 计算机、软件等专业编程能力较弱的在校学生
2. 各大OJ平台用户

### 2.4 约束和假设

1. 运行环境及硬件要求：本项目为借助python语言实现的简易WEB APP，绝大多数硬件环境均可正常运行，详见其他需求板块（4.3&&4.5）。
2. 法律相关：本项目旨在为学习编程技术人员提高解题帮助，无任何营销目的。用户借助本平台进行其他与项目需求无关行为，用户承担全部法律责任。

## 3. 功能需求

### 3.1 题目爬取与手动提交代码 

#### 3.1.1 欢迎界面

- 此页面为评测系统的主页，页面标题为“欢迎使用-XOJ”。


- 主页显示XOJ平台的logo、名称、简要介绍等信息。要求主界面元素居中布局，风格简约大方。
- 主页正中偏下处有一个按钮，显示文字为“进入系统”，点击后跳转到“题目列表”页面。

#### 3.1.2 题目列表 

- 页面标题为“题目列表-XOJ”
- 页面主题部分为一个列表，表格有如下几列，“评测平台”，“题目编号”，“题目标题”。
- 默认按题目编号从小到大排序，其中题目编号和题目标题均为超链接，点击之后都可以进入对应题目的详细信息页面。
- 在“评测平台”列的表头处有一个下拉列表，从中可以选择只查看指定平台的题目。
- 在“题目编号”和“题目标题”列的表头处分别有一个文本输入框，用户可以输入筛选条件，其中“题目编号”是精确查找，“题目标题是模糊查找”。当文本框失去焦点时自动检索，刷新显示。
- 测试阶段以北京大学POJ或杭州电子科技大学HDU为例，要求可扩展性要强，可以方便快速地将新的评测平台添加到系统中。

#### 3.1.3 题目详情

- 页面标题为“\<题目名称\>-\<评测平台\> \<题目编号\>-XOJ”。尖括号号中的内容根据不同的题目动态显示。
- 页面显示题目标题、运行时间内存限制要求、题目描述、输入格式、输出格式、样例输入、样例输出等信息，这些信息通过爬虫获得。最下方是一个按钮，显示文字为“提交”，点击之后进入“代码提交页面”。

#### 3.1.4 代码提交

- 页面标题为“提交-\<题目名称\>-\<评测平台\> \<题目编号\>-XOJ”。尖括号号中的内容根据不同的题目动态显示。
- 页面显示题目名称，题目编号等信息，显示一个下拉列表，从中可以选择使用的语言或编译器，列表中的内容由爬虫获取。中间部分是一个大的多行文本输入框，用户将要提交的代码粘贴在输入框中。最下方是一个按钮，显示文字为“提交”，点击之后系统将用户的代码发送到对用的评测平台，并跳转到“评测状态”页面。

#### 3.1.5 评测状态

- 页面标题为“评测状态-XOJ”。
- 页面主体部分为一个列表，有“评测平台”、“题目编号”、“题目描述”、“提交时间”、“代码长度”、“运行时间”、“评测状态”等几列，其中“题目编号”和“题目描述”均为超链接，点击之后可以跳转到“题目详情页面”，“评测状态”处会实时动态刷新，根据评测状态显示“正在提交”、“正在排队”、“WA错误的结果”、”AC完全通过“等状态。

### 3.2 自动搜索题解并批量提交代码

#### 3.2.1 选择题目

- 在”题目列表“点击”自动提交“按钮，点击之后列表中每道题左侧出现一个复选框，用户打勾就表明将这道题加入到自动提交队列中。此时仍然可以通过表头的文本框筛选想要的题目，页面上也会显示当前已经选择的题目数量。题目选择完毕后点击”自动提交“按钮跳转到”评测状态“页面。

#### 3.2.2 自动提交

- 选择的题目出现在”评测状态“页面的列表中，系统自动依次尝试每道题，如过选择

### 3.3 分析指定用户或题目数据 

#### 3.3.1 分析用户成长经历 

- 在“题目列表”页面点击“数据分析”按钮，跳转到“数据分析”页面。页面提示“请输入用户名”，用户输入用户名后点击旁边的“分析”按钮，平台自动在已有的平台平台中搜索当前用户的历史数据。
- 在页面中显示一个折线统计图，横轴为时间，纵轴为做题量，显示了用户从注册开始到现在为止的做题信息。
- 下方是一个表格，是折线统计图的具体化，分别有“提交时间”、“评测平台”、“题目编号”、题目名称“、”代码长度“、”占用内存“、”运行时间“、”评测结果“等列，同样用户可以在表头筛选选择特定的信息查看。

#### 3.3.2 分析题目难易情况

- 在“题目列表”页面点击“数据分析”按钮，跳转到“数据分析”页面。页面中有一个下拉列表，可以选择评测平台，在旁边的文本框中数据题目编号或者题目名称，点击”搜索“按钮，平台将搜索到的题目显示在下方，点击题目，进入”题目分析“页面。
- ”题目分析“页面中主体部分是一个表格，表中详细列出了与这道题目有关所有提交记录，并显示总的提交次数和通过次数，并据此给出题目难易情况的一个评估。用户同样可以筛选特定信息查看。

## 4. 其他需求

### 4.1 性能需求

为了能够快捷地提供服务，系统应该能够快速地响应查询请求。用户最终得到结果的响应时间除了与系统响应速度有关外，还与网络状况有关。对系统最低的要求是，在相关联的评测平台正常工作负荷下，能够容纳数百人的同时访问与手工提交。可以满足数十人同时使用自动提交功能。

### 4.2 安全需求

1. 网络安全：使用电信专线与边界防火墙接入保证网络安全。
2. 数据传输安全：传输的数据都采用加密算法加密，使得数据即使泄漏、被截获后，也无法识别相关的数据内容，确保数据安全。

### 4.3 硬件需求

本项目对硬件的要求不高，要求当下所有主流操作系统主流浏览器都可以正常使用。

### 4.4 网络需求

由于本项目需要在线判题，建议的网络速度是1MB/S，最低网络速度200KB/S。

### 4.5 运行环境

要求在当下主流的PC端和移动端均可以流畅访问，PC端如Windows系统、Linux系统、Mac OS X系统。移动终端如Android、iOS系统等。要求页面有媒体查询功能，根据设备屏幕的尺寸自动调节页面显示的内容。













