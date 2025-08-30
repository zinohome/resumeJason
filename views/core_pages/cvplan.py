from dash import html
import feffery_utils_components as fuc
import feffery_antd_components as fac  # 新增导入


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
                                    
                                    # 标题 - 修改为未来工作规划
                                    html.H1(
                                        '未来工作规划',
                                        style={
                                            'color': '#e02020',  # 红色标题
                                            'fontSize': '40px',
                                            'fontWeight': 'bold',
                                            'margin': '0',
                                            'lineHeight': '48px'
                                        }
                                    )
                                ],
                                style={
                                    'display': 'flex',
                                    'alignItems': 'center',
                                    'marginBottom': '40px'  # 减少标题下方留白，使内容更紧凑
                                }
                            ),
                            
                            # 未来工作规划内容区域
                            html.Div(
                                [
                                    # 顶部plan_top.png图片（扁长型）
                                    html.Div(
                                        style={
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center',
                                            'marginBottom': '50px',
                                            'position': 'relative'
                                        },
                                        children=[
                                            # 顶部大图片
                                            html.Img(
                                                src='/assets/imgs/plan_top.png',
                                                style={
                                                    'width': '90%',  # 增加宽度使图片更扁长
                                                    'height': 'auto',
                                                    'maxHeight': '240px',  # 减小最大高度使图片更扁平
                                                    'objectFit': 'contain'
                                                }
                                            )
                                        ]
                                    ),
                                    
                                    # 下方三张图片和文字说明（三列布局）
                                    html.Div(
                                        style={
                                            'display': 'flex',
                                            'justifyContent': 'space-between',
                                            'alignItems': 'flex-start',
                                            'width': '100%'
                                        },
                                        children=[
                                            # 近期规划 - plan_short.png
                                            html.Div(
                                                style={
                                                    'display': 'flex',
                                                    'flexDirection': 'column',
                                                    'alignItems': 'flex-start',  # 修改为左对齐
                                                    'width': '32%',
                                                    'textAlign': 'left',  # 修改为左对齐
                                                    'marginBottom': '20px'
                                                },
                                                children=[
                                                    # 近期文字描述 - 添加图标
                                                    html.Div(
                                                        style={
                                                            'display': 'flex',
                                                            'alignItems': 'flex-start',
                                                            'marginBottom': '20px',
                                                            'width': '100%'
                                                        },
                                                        children=[
                                                            # AntdIcon图标
                                                            fac.AntdIcon(
                                                                icon='bs-list-task',
                                                                style={
                                                                    'color': '#1890ff',
                                                                    'fontSize': '18px',
                                                                    'marginRight': '10px',
                                                                    'marginTop': '2px'
                                                                }
                                                            ),
                                                            # 文字内容
                                                            html.P(
                                                                '梳理当前数据中心运维价值目标和服务链路，构建全面的运维体系和服务保障能力。',
                                                                style={
                                                                    'fontFamily': 'Microsoft YaHei',
                                                                    'fontSize': '16px',
                                                                    'color': '#333',
                                                                    'margin': '0',
                                                                    'lineHeight': '1.5',
                                                                    'flex': '1'
                                                                }
                                                            )
                                                        ]
                                                    ),
                                                    # 近期图片（较大尺寸）
                                                    html.Img(
                                                        src='/assets/imgs/plan_short.png',
                                                        style={
                                                            'width': '100%',
                                                            'height': 'auto',
                                                            'objectFit': 'contain',
                                                            'maxHeight': '380px'  # 增加最大高度使图片更大
                                                        }
                                                    )
                                                ]
                                            ),
                                            
                                            # 中期规划 - plan_middle.png
                                            html.Div(
                                                style={
                                                    'display': 'flex',
                                                    'flexDirection': 'column',
                                                    'alignItems': 'flex-start',  # 修改为左对齐
                                                    'width': '32%',
                                                    'textAlign': 'left',  # 修改为左对齐
                                                    'marginBottom': '20px'
                                                },
                                                children=[
                                                    # 中期文字描述 - 添加图标
                                                    html.Div(
                                                        style={
                                                            'display': 'flex',
                                                            'alignItems': 'flex-start',
                                                            'marginBottom': '20px',
                                                            'width': '100%'
                                                        },
                                                        children=[
                                                            # AntdIcon图标
                                                            fac.AntdIcon(
                                                                icon='bs-list-task',
                                                                style={
                                                                    'color': '#52c41a',
                                                                    'fontSize': '18px',
                                                                    'marginRight': '10px',
                                                                    'marginTop': '2px'
                                                                }
                                                            ),
                                                            # 文字内容
                                                            html.P(
                                                                '整体规划设计并构建基于SRE的智能运维管理平台，实现数据中心运维服务能力的本质提升。',
                                                                style={
                                                                    'fontFamily': 'Microsoft YaHei',
                                                                    'fontSize': '16px',
                                                                    'color': '#333',
                                                                    'margin': '0',
                                                                    'lineHeight': '1.5',
                                                                    'flex': '1'
                                                                }
                                                            )
                                                        ]
                                                    ),
                                                    # 中期图片（较大尺寸）
                                                    html.Img(
                                                        src='/assets/imgs/plan_middle.png',
                                                        style={
                                                            'width': '100%',
                                                            'height': 'auto',
                                                            'objectFit': 'contain',
                                                            'maxHeight': '380px'  # 增加最大高度使图片更大
                                                        }
                                                    )
                                                ]
                                            ),
                                            
                                            # 长期规划 - plan_long.png
                                            html.Div(
                                                style={
                                                    'display': 'flex',
                                                    'flexDirection': 'column',
                                                    'alignItems': 'flex-start',  # 修改为左对齐
                                                    'width': '32%',
                                                    'textAlign': 'left',  # 修改为左对齐
                                                    'marginBottom': '20px'
                                                },
                                                children=[
                                                    # 长期文字描述 - 添加图标
                                                    html.Div(
                                                        style={
                                                            'display': 'flex',
                                                            'alignItems': 'flex-start',
                                                            'marginBottom': '20px',
                                                            'width': '100%'
                                                        },
                                                        children=[
                                                            # AntdIcon图标
                                                            fac.AntdIcon(
                                                                icon='bs-list-task',
                                                                style={
                                                                    'color': '#faad14',
                                                                    'fontSize': '18px',
                                                                    'marginRight': '10px',
                                                                    'marginTop': '2px'
                                                                }
                                                            ),
                                                            # 文字内容
                                                            html.P(
                                                                '从五个维度和八个关键点出发，迭代优化基于CSMO框架的智能运维管理平台，以打造基于稳态下的运维管理新体系。',
                                                                style={
                                                                    'fontFamily': 'Microsoft YaHei',
                                                                    'fontSize': '16px',
                                                                    'color': '#333',
                                                                    'margin': '0',
                                                                    'lineHeight': '1.5',
                                                                    'flex': '1'
                                                                }
                                                            )
                                                        ]
                                                    ),
                                                    # 长期图片（较大尺寸）
                                                    html.Img(
                                                        src='/assets/imgs/plan_long.png',
                                                        style={
                                                            'width': '100%',
                                                            'height': 'auto',
                                                            'objectFit': 'contain',
                                                            'maxHeight': '380px'  # 增加最大高度使图片更大
                                                        }
                                                    )
                                                ]
                                            )
                                        ]
                                    )
                                ],
                                style={
                                    'width': '100%',
                                    'padding': '20px 0'
                                }
                            )
                        ],
                        style={
                            'width': '100%',
                            'padding': '20px 0'
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