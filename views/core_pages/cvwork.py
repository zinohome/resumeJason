from dash import html
import feffery_utils_components as fuc
import feffery_antd_components as fac


def render_header():
    """渲染页面头部，包含标题和logo"""
    return html.Div(
        [
            # 右上角logo
            html.Div(
                        [
                            html.A(
                                href='/core/cvagenda',
                                target='_self',
                                children=[
                                    html.Img(
                                        src='/assets/imgs/zjlab-logo.png',
                                        style={
                                            'height': '100px',  # 保持logo比例
                                            'objectFit': 'contain',
                                            'verticalAlign': 'middle'
                                        }
                                    )
                                ]
                            )
                        ],
                        style={
                            'position': 'absolute',
                            'top': '20px',
                            'right': '40px',
                            'zIndex': '10',
                            'display': 'flex',
                            'alignItems': 'center'
                        }
                    ),
            # 标题区域
            html.Div(
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'marginBottom': '30px',
                    'marginTop': '20px'
                },
                children=[
                    html.Div(
                        style={
                            'width': '0',
                            'height': '0',
                            'borderLeft': '15px solid transparent',
                            'borderRight': '15px solid transparent',
                            'borderBottom': '26px solid #e02020',
                            'marginRight': '15px'
                        }
                    ),
                    html.H1(
                        '基本情况介绍',
                        style={
                            'color': '#333',
                            'fontSize': '24px',
                            'fontWeight': 'bold',
                            'margin': '0',
                            'fontFamily': 'Microsoft YaHei'
                        }
                    )
                ]
            )
        ]
    )


# 新的四栏内容区域实现
def render_development_section():
    """渲染开发部分"""
    return html.Div(
        style={
            'flex': '1',
            'padding': '0 15px',
            'display': 'flex',
            'flexDirection': 'column'
        },
        children=[
            # 标题区域
            html.Div(
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'marginBottom': '15px',
                    'borderBottom': '2px solid #e0e0e0',
                    'paddingBottom': '10px'
                },
                children=[
                    # 图标
                    fac.AntdIcon(
                        icon='pi-buildings',
                        style={'width': '20px', 'height': '20px', 'color': '#1890ff'}
                    ),
                    html.H3(
                        '开发',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '18px',
                            'color': '#333',
                            'margin': '0'
                        }
                    )
                ]
            ),
            # 内容区域
            html.Div(
                style={'marginBottom': '20px'},
                children=[
                    html.P(
                        '主要开发语言：Java、Python',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 10px 0',
                            'color': '#333'
                        }
                    ),
                    html.P(
                        '当前在用：',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#333'
                        }
                    ),
                    html.P(
                        '• 基于产品的定制：2 套：某部委、某运动品牌；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#666'
                        }
                    ),
                    html.P(
                        '• 平台类：3 套（大数据平台、开源治理平台、自动化运维平台）：政府、车企、多家银行；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#666'
                        }
                    ),
                    html.P(
                        '• 内部使用：6套：资产平台、运维专家系统、内部运营平台；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#666'
                        }
                    ),
                    html.P(
                        '• IOT、AI类：3套：交通、医疗、云企业；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0',
                            'color': '#666'
                        }
                    )
                ]
            ),
            # 图片区域
            html.Div(
                children=[
                    html.Img(
                        src='/assets/imgs/develop1.png',
                        style={
                            'width': '100%',
                            'height': 'auto',
                            'marginBottom': '10px',
                            'border': '1px solid #ddd'
                        }
                    ),
                    # 注意：develop2可能是一个文件夹，这里使用占位图
                    html.Img(
                        src='/assets/imgs/develop2.png',
                        style={
                            'width': '100%',
                            'height': 'auto',
                            'border': '1px solid #ddd'
                        }
                    )
                ]
            )
        ]
    )


def render_maintenance_section():
    """渲染运维部分"""
    return html.Div(
        style={
            'flex': '1',
            'padding': '0 15px',
            'display': 'flex',
            'flexDirection': 'column'
        },
        children=[
            # 标题区域
            html.Div(
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'marginBottom': '15px',
                    'borderBottom': '2px solid #e0e0e0',
                    'paddingBottom': '10px'
                },
                children=[
                    # 图标
                    fac.AntdIcon(
                        icon='pi-buildings',
                        style={'width': '20px', 'height': '20px', 'color': '#52c41a'}
                    ),
                    html.H3(
                        '运维',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '18px',
                            'color': '#333',
                            'margin': '0'
                        }
                    )
                ]
            ),
            # 内容区域
            html.Div(
                style={'marginBottom': '20px', 'minHeight': '200px'},
                children=[
                    html.P(
                        '主要负责：',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#333'
                        }
                    ),
                    html.P(
                        '• 大型银行、通讯公司多年运维支持、迁移、灾备建设和系统架构优化；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#666'
                        }
                    ),
                    html.P(
                        '-- 重点事件：2010-2013年银行、保险、交管全国业务上收和大集中；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#666'
                        }
                    ),
                    html.P(
                        '• 混合云容器平台运维：某消费品头部客户；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#666'
                        }
                    ),
                    html.P(
                        '• 头部商业银行云平台及分布式核心系统运维体系设计；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0',
                            'color': '#666'
                        }
                    )
                ]
            ),
            # 图片区域
            html.Div(
                children=[
                    html.Img(
                        src='/assets/imgs/maintenance1.png',
                        style={
                            'width': '100%',
                            'height': 'auto',
                            'marginBottom': '10px',
                            'border': '1px solid #ddd'
                        }
                    ),
                    html.Img(
                        src='/assets/imgs/maintenance2.png',
                        style={
                            'width': '100%',
                            'height': 'auto',
                            'border': '1px solid #ddd'
                        }
                    )
                ]
            )
        ]
    )


def render_architecture_section():
    """渲染架构部分"""
    return html.Div(
        style={
            'flex': '1',
            'padding': '0 15px',
            'display': 'flex',
            'flexDirection': 'column'
        },
        children=[
            # 标题区域
            html.Div(
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'marginBottom': '15px',
                    'borderBottom': '2px solid #e0e0e0',
                    'paddingBottom': '10px'
                },
                children=[
                    # 图标
                    fac.AntdIcon(
                        icon='pi-buildings',
                        style={'width': '20px', 'height': '20px', 'color': '#faad14'}
                    ),
                    html.H3(
                        '架构',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '18px',
                            'color': '#333',
                            'margin': '0'
                        }
                    )
                ]
            ),
            # 内容区域
            html.Div(
                style={'marginBottom': '20px', 'minHeight': '200px'},
                children=[
                    html.P(
                        '主导规划设计：',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#333'
                        }
                    ),
                    html.P(
                        '• 头部企业混合云大数据平台建设；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#666'
                        }
                    ),
                    html.P(
                        '• 工业互联网平台数据体系建设；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#666'
                        }
                    ),
                    html.P(
                        '• 金融行业客户多云平台架构及运维体系设计；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#666'
                        }
                    ),
                    html.P(
                        '• 多家两地三中心灾备体系设计；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0',
                            'color': '#666'
                        }
                    )
                ]
            ),
            # 图片区域
            html.Div(
                children=[
                    html.Img(
                        src='/assets/imgs/architect1.png',
                        style={
                            'width': '100%',
                            'height': 'auto',
                            'marginBottom': '10px',
                            'border': '1px solid #ddd'
                        }
                    ),
                    html.Img(
                        src='/assets/imgs/architect2.png',
                        style={
                            'width': '100%',
                            'height': 'auto',
                            'border': '1px solid #ddd'
                        }
                    )
                ]
            )
        ]
    )


def render_consulting_section():
    """渲染咨询部分"""
    return html.Div(
        style={
            'flex': '1',
            'padding': '0 15px',
            'display': 'flex',
            'flexDirection': 'column'
        },
        children=[
            # 标题区域
            html.Div(
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'marginBottom': '15px',
                    'borderBottom': '2px solid #e0e0e0',
                    'paddingBottom': '10px'
                },
                children=[
                    # 图标
                    fac.AntdIcon(
                        icon='pi-buildings',
                        style={'width': '20px', 'height': '20px', 'color': '#f5222d'}
                    ),
                    html.H3(
                        '咨询',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '18px',
                            'color': '#333',
                            'margin': '0'
                        }
                    )
                ]
            ),
            # 内容区域
            html.Div(
                style={'marginBottom': '20px', 'minHeight': '200px'},
                children=[
                    html.P(
                        '主导规划设计：',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#333'
                        }
                    ),
                    html.P(
                        '• 头部企业混合云大数据平台建设；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#666'
                        }
                    ),
                    html.P(
                        '• 工业互联网平台数据体系建设；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#666'
                        }
                    ),
                    html.P(
                        '• 金融行业客户多云平台架构及运维体系设计；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0 0 5px 0',
                            'color': '#666'
                        }
                    ),
                    html.P(
                        '• 多家两地三中心灾备体系设计；',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'margin': '0',
                            'color': '#666'
                        }
                    )
                ]
            ),
            # 图片区域
            html.Div(
                children=[
                    html.Img(
                        src='/assets/imgs/consultant1.png',
                        style={
                            'width': '100%',
                            'height': 'auto',
                            'marginBottom': '10px',
                            'border': '1px solid #ddd'
                        }
                    ),
                    html.Img(
                        src='/assets/imgs/consultant2.png',
                        style={
                            'width': '100%',
                            'height': 'auto',
                            'border': '1px solid #ddd'
                        }
                    )
                ]
            )
        ]
    )


def render_left_section():
    """渲染左侧区域：空，因为我们要实现四栏布局"""
    return html.Div()


def render_right_section():
    """渲染右侧区域：四栏内容布局"""
    return html.Div(
        style={
            'width': '100%',
            'display': 'flex',
            'flexDirection': 'row',
            'flexWrap': 'wrap'
        },
        children=[
            render_development_section(),
            render_maintenance_section(),
            render_architecture_section(),
            render_consulting_section()
        ]
    )


def render():
    """子页面：简历信息页面 - 按照cvagenda.py的布局结构实现"""
    
    return html.Div(
        [
            # 使用FefferyDiv作为内容区域容器，添加阴影效果
            fuc.FefferyDiv(
                [
                    # 右上角logo
                    html.Div(
                        [
                            html.A(
                                href='/core/cvagenda',
                                target='_self',
                                children=[
                                    html.Img(
                                        src='/assets/imgs/zjlab-logo.png',
                                        style={
                                            'height': '100px',  # 保持logo比例
                                            'objectFit': 'contain',
                                            'verticalAlign': 'middle'
                                        }
                                    )
                                ]
                            )
                        ],
                        style={
                            'position': 'absolute',
                            'top': '20px',
                            'right': '40px',
                            'zIndex': '10',
                            'display': 'flex',
                            'alignItems': 'center'
                        }
                    ),
                    
                    # 主内容区域 - 标题和内容
                    html.Div(
                        [
                            # 左侧红色竖条和标题
                            html.Div(
                                [
                                    # 左侧红色竖条（与标题等高）
                                    html.Div(
                                        style={
                                            'backgroundColor': '#e02020',  # 红色背景
                                            'width': '15px',
                                            'height': '48px',  # 与标题高度一致
                                            'marginRight': '20px'
                                        }
                                    ),
                                    
                                    # 标题 - 修改为'主要工作业绩'
                                    html.H1(
                                        '主要工作业绩',
                                        style={
                                            'color': '#e02020',  # 红色标题
                                            'fontSize': '40px',
                                            'fontWeight': 'bold',
                                            'margin': '0',
                                            'fontFamily': '方正小标宋简体, sans-serif',
                                            'lineHeight': '48px'
                                        }
                                    )
                                ],
                                style={
                                    'display': 'flex',
                                    'alignItems': 'center',
                                    'marginBottom': '5px'
                                }
                            ),
                            
                            # 左侧和右侧内容区域
                            html.Div(
                                [
                                    # 左侧区域
                                    render_left_section(),
                                    
                                    # 右侧区域 - 四栏布局
                                    render_right_section()
                                ],
                                style={
                                    'display': 'flex',
                                    'alignItems': 'flex-start',
                                    'width': '100%',
                                    'paddingTop': '20px'
                                }
                            )
                        ],
                        style={
                            'width': '100%',
                            'height': '100%',
                            'padding': '60px 80px 40px 80px'  # 上下左右内边距
                        }
                    ),
                    
                    # 底部彩色条纹
                    html.Div(
                        style={
                            'position': 'absolute',
                            'bottom': '0',
                            'left': '0',
                            'width': '100%',
                            'height': '8px',
                            'background': 'linear-gradient(90deg, #1a365d 0%, #1a365d 11.1%, #1a365d 11.1%, #1a465d 22.2%, #1a565d 22.2%, #1a565d 33.3%, #1a665d 33.3%, #1a665d 44.4%, #1a765d 44.4%, #1a765d 55.5%, #1a865d 55.5%, #1a865d 66.6%, #1a965d 66.6%, #1a965d 77.7%, #1aa65d 77.7%, #1aa65d 100%)'
                        }
                    )
                ],
                # FefferyDiv的阴影效果配置
                shadow='always-shadow-light',
                style={
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'overflow': 'hidden',
                    'display': 'flex',
                    'position': 'relative'  # 为绝对定位的元素提供参考
                }
            )
        ],
        # 整体页面样式
        style={
            'margin': '0',
            'padding': '40px',  # 添加内边距以显示灰色背景
            'width': '100%',
            'height': '100vh',
            'backgroundColor': '#f0f0f0',  # 整体页面灰色背景
            'boxSizing': 'border-box',
            'display': 'flex',
            'alignItems': 'center',
            'justifyContent': 'center'
        }
    )