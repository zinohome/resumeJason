from dash import html
import feffery_utils_components as fuc
import feffery_antd_components as fac  # 新增导入


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


def render_left_section():
    """渲染左侧区域：照片、姓名、教育经历和证书"""
    return html.Div(
        style={
            'flex': '0.4',
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center'
        },
        children=[
            # 照片区域
            html.Div(
                style={
                    'width': '180px',
                    'height': '180px',
                    'borderRadius': '50%',
                    'overflow': 'hidden',
                    'marginBottom': '20px',
                    'border': '2px solid #ddd'
                },
                children=[
                    html.Img(
                        src='/assets/imgs/zhangjun.png',  # 使用参考图片中显示的正确路径
                        style={'width': '100%', 'height': '100%', 'objectFit': 'cover'}
                    )
                ]
            ),
            # 姓名
            html.H2(
                '张俊',
                style={
                    'fontFamily': 'Microsoft YaHei',
                    'fontSize': '24px',
                    'color': '#1a365d',
                    'margin': '0 0 30px 0'
                }
            ),
            # 教育经历
            html.Div(
                style={
                    'width': '100%',
                    'marginBottom': '30px'
                },
                children=[
                    html.Div(
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'marginBottom': '15px',
                            'borderBottom': '2px solid #e0e0e0',
                            'paddingBottom': '10px'
                        },
                        children=[
                            # 替换为AntdIcon
                            fac.AntdIcon(
                                icon='md-layers',
                                style={'width': '30px', 'height': '30px', 'marginRight': '10px', 'color': '#1890ff'}
                            ),
                            html.H3(
                                '教育经历',
                                style={
                                    'fontFamily': 'Microsoft YaHei',
                                    'fontSize': '18px',
                                    'color': '#333',
                                    'margin': '0'
                                }
                            )
                        ]
                    ),
                    html.P(
                        '1997.9-2001.7 青岛建筑工程学院',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '16px',
                            'lineHeight': '1.6',
                            'margin': '0 0 5px 0',
                            'color': '#333'
                        }
                    ),
                    html.P(
                        '统计学 | 本科',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '16px',
                            'lineHeight': '1.6',
                            'margin': '0',
                            'color': '#666'
                        }
                    )
                ]
            ),
            # 证书
            html.Div(
                style={'width': '100%'},
                children=[
                    html.Div(
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'marginBottom': '15px',
                            'borderBottom': '2px solid #e0e0e0',
                            'paddingBottom': '10px'
                        },
                        children=[
                            # 替换为AntdIcon
                            fac.AntdIcon(
                                icon='md-extension',
                                style={'width': '30px', 'height': '30px', 'marginRight': '10px', 'color': '#52c41a'}
                            ),
                            html.H3(
                                '证书',
                                style={
                                    'fontFamily': 'Microsoft YaHei',
                                    'fontSize': '18px',
                                    'color': '#333',
                                    'margin': '0'
                                }
                            )
                        ]
                    ),
                    html.P(
                        '参与通信AI《AI时代的IT架构建设与智慧运维服务》白皮书撰写',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'lineHeight': '1.6',
                            'margin': '0 0 5px 0',
                            'color': '#333'
                        }
                    ),
                    html.P(
                        'TOGAF、COBIT、企业数据治理专家、PMP',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'lineHeight': '1.6',
                            'margin': '0',
                            'color': '#666'
                        }
                    )
                ]
            )
        ]
    )


def render_right_section():
    """渲染右侧区域：自我评价和工作经历"""
    return html.Div(
        style={
            'flex': '0.6',
            'display': 'flex',
            'flexDirection': 'column'
        },
        children=[
            # 自我评价
            html.Div(
                style={
                    'marginBottom': '30px',
                    'padding': '15px',
                    'backgroundColor': '#f8f8f8',
                    'borderRadius': '5px'
                },
                children=[
                    html.Div(
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'marginBottom': '15px',
                            'borderBottom': '2px solid #e0e0e0',  # 新增横线样式
                            'paddingBottom': '10px'  # 新增底部内边距
                        },
                        children=[
                            fac.AntdIcon(
                                icon='md-pin-drop',
                                style={'width': '30px', 'height': '30px', 'marginRight': '10px', 'color': '#faad14'}
                            ),
                            html.H3(
                                '自我评价',
                                style={
                                    'fontFamily': 'Microsoft YaHei',
                                    'fontSize': '18px',
                                    'color': '#333',
                                    'margin': '0'
                                }
                            )
                        ]
                    ),
                    html.P(
                        'IBM Band9 IT技术咨询专家，具备20年以上大客户及大型平台架构规划设计、实施交付、运营运维经验。',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'lineHeight': '1.8',
                            'margin': '0 0 10px 0',
                            'color': '#333'
                        }
                    ),
                    html.P(
                        '长期服务多重大型政企用户实施数字化创新升级，推动数字技术与业务的深度融合。',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'lineHeight': '1.8',
                            'margin': '0 0 10px 0',
                            'color': '#333'
                        }
                    ),
                    html.P(
                        '在大数据中心解决方案、混合云架构、容灾与业务连续性管理等领域深耕多年，聚焦把握大行业算力中心精准选建、自动化运维与基础设施优化，保障核心业务信息高效运行。',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'lineHeight': '1.8',
                            'margin': '0 0 10px 0',
                            'color': '#333'
                        }
                    ),
                    html.P(
                        '精通企业级大数据平台与数据运营管理，具备主流大模型及AI平台（如OpenAI、阿里云百炼等）企业集成及创新应用能力。',
                        style={
                            'fontFamily': 'Microsoft YaHei',
                            'fontSize': '14px',
                            'lineHeight': '1.8',
                            'margin': '0',
                            'color': '#333'
                        }
                    )
                ]
            ),
            html.Div(
                style={
                    'marginTop': '-6px',  # 向上移动10px使其与教育经历横线对齐
                    'marginBottom': '0',   # 确保没有额外的底部边距影响对齐
                },
                children=[
                    html.Div(
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'marginBottom': '20px',
                            'borderBottom': '2px solid #e0e0e0',
                            'paddingBottom': '10px'
                        },
                        children=[
                            fac.AntdIcon(
                                icon='md-people',
                                style={'width': '30px', 'height': '30px', 'marginRight': '10px', 'color': '#f5222d'}
                            ),
                            html.H3(
                                '工作经历',
                                style={
                                    'fontFamily': 'Microsoft YaHei',
                                    'fontSize': '18px',
                                    'color': '#333',
                                    'margin': '0'
                                }
                            )
                        ]
                    ),
                    html.Div(
                        style={
                            'position': 'relative',
                            'paddingLeft': '30px'
                        },
                        children=[
                            # 工作经历条目1
                            html.Div(
                                style={'marginBottom': '25px'},
                                children=[
                                    # 时间节点
                                    html.Div(
                                        style={
                                            'position': 'absolute',
                                            'left': '0',
                                            'top': '5px',
                                            'width': '12px',
                                            'height': '12px',
                                            'borderRadius': '50%',
                                            'backgroundColor': '#e02020',
                                            'zIndex': '2'
                                        }
                                    ),
                                    # 连接线
                                    html.Div(
                                        style={
                                            'position': 'absolute',
                                            'left': '5px',
                                            'top': '17px',
                                            'width': '2px',
                                            'height': '260px',  # 调整高度以覆盖所有5个条目
                                            'backgroundColor': '#ddd'
                                        }
                                    ),
                                    html.P(
                                        '2021.11至今 某公司 IT架构总监',
                                        style={
                                            'fontFamily': 'Microsoft YaHei',
                                            'fontSize': '16px',
                                            'fontWeight': 'bold',
                                            'margin': '0 0 5px 0',
                                            'color': '#333'
                                        }
                                    ),
                                    html.P(
                                        '负责公司整体IT战略规划与实施，推动数字化转型，管理IT架构团队。',
                                        style={
                                            'fontFamily': 'Microsoft YaHei',
                                            'fontSize': '14px',
                                            'margin': '0',
                                            'color': '#666'
                                        }
                                    )
                                ]
                            ),
                            # 工作经历条目2
                            html.Div(
                                style={'marginBottom': '25px'},
                                children=[
                                    # 时间节点
                                    html.Div(
                                        style={
                                            'position': 'absolute',
                                            'left': '0',
                                            'top': '75px',
                                            'width': '12px',
                                            'height': '12px',
                                            'borderRadius': '50%',
                                            'backgroundColor': '#e02020',
                                            'zIndex': '2'
                                        }
                                    ),
                                    html.P(
                                        '2015.3-2021.10 某科技公司 高级架构师',
                                        style={
                                            'fontFamily': 'Microsoft YaHei',
                                            'fontSize': '16px',
                                            'fontWeight': 'bold',
                                            'margin': '0 0 5px 0',
                                            'color': '#333'
                                        }
                                    ),
                                    html.P(
                                        '负责大型云计算平台架构设计与优化，推动微服务转型。',
                                        style={
                                            'fontFamily': 'Microsoft YaHei',
                                            'fontSize': '14px',
                                            'margin': '0',
                                            'color': '#666'
                                        }
                                    )
                                ]
                            ),
                            # 工作经历条目3
                            html.Div(
                                style={'marginBottom': '25px'},
                                children=[
                                    # 时间节点
                                    html.Div(
                                        style={
                                            'position': 'absolute',
                                            'left': '0',
                                            'top': '145px',
                                            'width': '12px',
                                            'height': '12px',
                                            'borderRadius': '50%',
                                            'backgroundColor': '#e02020',
                                            'zIndex': '2'
                                        }
                                    ),
                                    html.P(
                                        '2001.7-2015.2 英国某企业 技术经理',
                                        style={
                                            'fontFamily': 'Microsoft YaHei',
                                            'fontSize': '16px',
                                            'fontWeight': 'bold',
                                            'margin': '0 0 5px 0',
                                            'color': '#333'
                                        }
                                    ),
                                    html.P(
                                        '负责企业应用系统规划、设计与实施，管理技术团队。',
                                        style={
                                            'fontFamily': 'Microsoft YaHei',
                                            'fontSize': '14px',
                                            'margin': '0',
                                            'color': '#666'
                                        }
                                    )
                                ]
                            ),
                            # 工作经历条目4
                            html.Div(
                                style={'marginBottom': '25px'},
                                children=[
                                    # 时间节点
                                    html.Div(
                                        style={
                                            'position': 'absolute',
                                            'left': '0',
                                            'top': '215px',
                                            'width': '12px',
                                            'height': '12px',
                                            'borderRadius': '50%',
                                            'backgroundColor': '#e02020',
                                            'zIndex': '2'
                                        }
                                    ),
                                    html.P(
                                        '1998.8-2001.6 某软件公司 程序员',
                                        style={
                                            'fontFamily': 'Microsoft YaHei',
                                            'fontSize': '16px',
                                            'fontWeight': 'bold',
                                            'margin': '0 0 5px 0',
                                            'color': '#333'
                                        }
                                    ),
                                    html.P(
                                        '参与企业管理软件的开发与测试，编写技术文档。',
                                        style={
                                            'fontFamily': 'Microsoft YaHei',
                                            'fontSize': '14px',
                                            'margin': '0',
                                            'color': '#666'
                                        }
                                    )
                                ]
                            ),
                            # 工作经历条目5
                            html.Div(
                                children=[
                                    # 时间节点
                                    html.Div(
                                        style={
                                            'position': 'absolute',
                                            'left': '0',
                                            'top': '285px',
                                            'width': '12px',
                                            'height': '12px',
                                            'borderRadius': '50%',
                                            'backgroundColor': '#e02020',
                                            'zIndex': '2'
                                        }
                                    ),
                                    html.P(
                                        '1997.9-1998.7 某大学 助教',
                                        style={
                                            'fontFamily': 'Microsoft YaHei',
                                            'fontSize': '16px',
                                            'fontWeight': 'bold',
                                            'margin': '0 0 5px 0',
                                            'color': '#333'
                                        }
                                    ),
                                    html.P(
                                        '协助教授进行教学工作，参与科研项目的数据处理。',
                                        style={
                                            'fontFamily': 'Microsoft YaHei',
                                            'fontSize': '14px',
                                            'margin': '0',
                                            'color': '#666'
                                        }
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
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
                                    
                                    # 标题
                                    html.H1(
                                        '基本情况介绍',
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
                                    'marginBottom': '80px'
                                }
                            ),
                            
                            # 左侧和右侧内容区域
                            html.Div(
                                [
                                    # 左侧区域
                                    render_left_section(),
                                    
                                    # 右侧区域
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