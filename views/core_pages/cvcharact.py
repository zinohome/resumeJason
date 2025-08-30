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

                                    # 标题 - 修改为个人优势
                                    html.H1(
                                        '个人优势',
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
                                    'marginBottom': '40px'  # 减少标题下方留白，从80px改为40px
                                }
                            ),

                            # 圆形布局内容区域
                            html.Div(
                                style={
                                    'width': '100%',
                                    'height': '500px',  # 固定高度以容纳圆形布局
                                    'display': 'flex',
                                    'alignItems': 'center',
                                    'justifyContent': 'center',
                                    'position': 'relative',
                                    #'backgroundColor': 'white',
                                    'padding': '30px'
                                },
                                children=[
                                    # 中央核心能力区域（多层背景图）
                                    html.Div(
                                        style={
                                            'position': 'absolute',
                                            'width': '300px',
                                            'height': '300px',
                                            'display': 'flex',
                                            'alignItems': 'center',
                                            'justifyContent': 'center'
                                        },
                                        children=[
                                            # 核心能力背景层1 - blue
                                            html.Img(
                                                src='/assets/imgs/core_skills_bg1.png',
                                                style={
                                                    'position': 'absolute',
                                                    'width': '360px',
                                                    'height': '360px',
                                                    'zIndex': '1'
                                                }
                                            ),
                                            # 核心能力内容图片
                                            html.Img(
                                                src='/assets/imgs/core_skills.png',
                                                style={
                                                    'position': 'absolute',
                                                    'width': '200px',
                                                    'height': '120px',
                                                    'zIndex': '6'
                                                }
                                            )
                                        ]
                                    ),
                                    
                                    # 左侧弧形线条
                                    html.Img(
                                        src='/assets/imgs/arch_left.png',
                                        style={
                                            'position': 'absolute',
                                            'left': '15%',
                                            'top': '50%',
                                            'transform': 'translateY(-50%)',
                                            'width': '126px',
                                            'height': '560px',
                                            'zIndex': '7'
                                        }
                                    ),
                                    
                                    # 右侧弧形线条
                                    html.Img(
                                        src='/assets/imgs/arch_right.png',
                                        style={
                                            'position': 'absolute',
                                            'right': '15%',
                                            'top': '50%',
                                            'transform': 'translateY(-50%)',
                                            'width': '126px',
                                            'height': '560px',
                                            'zIndex': '7'
                                        }
                                    ),
                                    
                                    # 个人业务领域模块
                                    html.Div(
                                        style={
                                            'position': 'absolute',
                                            'left': '13%',
                                            'top': '25%',  # 调整垂直位置使其落在弧形线上
                                            'zIndex': '8'
                                        },
                                        children=[
                                            # 图标和文字水平布局容器
                                            html.Div(
                                                style={
                                                    'display': 'flex',
                                                    'alignItems': 'center',
                                                },
                                                children=[
                                                    # 图标容器
                                                    html.Div(
                                                        style={
                                                            'position': 'relative',
                                                            'marginRight': '15px',  # 图标与文字之间的间距
                                                            'display': 'flex',
                                                            'alignItems': 'center',
                                                            'justifyContent': 'center'
                                                        },
                                                        children=[
                                                            # 图标背景
                                                            html.Img(
                                                                src='/assets/imgs/ico_bg.png',
                                                                style={'width': '80px', 'height': '80px'}
                                                            ),
                                                            # 图标
                                                            html.Img(
                                                                src='/assets/imgs/ico_person.png',
                                                                style={
                                                                    'position': 'absolute',
                                                                    'width': '30px',
                                                                    'height': '30px'
                                                                }
                                                            )
                                                        ]
                                                    ),
                                                    # 文字内容容器
                                                    html.Div(
                                                        style={
                                                            'display': 'flex',
                                                            'flexDirection': 'column',
                                                            'justifyContent': 'center',
                                                            'minWidth': '200px'
                                                        },
                                                        children=[
                                                            # 标题
                                                            html.H3(
                                                                '个人业务领域',
                                                                style={
                                                                    'fontFamily': 'Microsoft YaHei',
                                                                    'fontSize': '16px',
                                                                    'color': '#333',
                                                                    'margin': '0 0 10px 0'
                                                                }
                                                            ),
                                                            # 描述
                                                            html.P(
                                                                '长期服务于关键行业百万级用户和头部企业的核心生产系统运维',
                                                                style={
                                                                    'fontFamily': 'Microsoft YaHei',
                                                                    'fontSize': '14px',
                                                                    'color': '#666',
                                                                    'margin': '0',
                                                                    'textAlign': 'left',  # 文字左对齐
                                                                    'width': '200px'
                                                                }
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                        ]
                                    ),
                                    
                                    # 专业技能模块
                                    html.Div(
                                        style={
                                            'position': 'absolute',
                                            'left': '13%',
                                            'bottom': '25%',  # 调整垂直位置使其落在弧形线上
                                            'zIndex': '8'
                                        },
                                        children=[
                                            # 图标和文字水平布局容器
                                            html.Div(
                                                style={
                                                    'display': 'flex',
                                                    'alignItems': 'center',
                                                },
                                                children=[
                                                    # 图标容器
                                                    html.Div(
                                                        style={
                                                            'position': 'relative',
                                                            'marginRight': '15px',  # 图标与文字之间的间距
                                                            'display': 'flex',
                                                            'alignItems': 'center',
                                                            'justifyContent': 'center'
                                                        },
                                                        children=[
                                                            # 图标背景
                                                            html.Img(
                                                                src='/assets/imgs/ico_bg.png',
                                                                style={'width': '80px', 'height': '80px'}
                                                            ),
                                                            # 图标
                                                            html.Img(
                                                                src='/assets/imgs/ico_professonal.png',
                                                                style={
                                                                    'position': 'absolute',
                                                                    'width': '30px',
                                                                    'height': '30px'
                                                                }
                                                            )
                                                        ]
                                                    ),
                                                    # 文字内容容器
                                                    html.Div(
                                                        style={
                                                            'display': 'flex',
                                                            'flexDirection': 'column',
                                                            'justifyContent': 'center',
                                                            'minWidth': '200px'
                                                        },
                                                        children=[
                                                            # 标题
                                                            html.H3(
                                                                '专业技能',
                                                                style={
                                                                    'fontFamily': 'Microsoft YaHei',
                                                                    'fontSize': '16px',
                                                                    'color': '#333',
                                                                    'margin': '0 0 10px 0'
                                                                }
                                                            ),
                                                            # 描述
                                                            html.P(
                                                                '具备大规模数据中心的自动化运维、故障自愈与高可用保障实战能力',
                                                                style={
                                                                    'fontFamily': 'Microsoft YaHei',
                                                                    'fontSize': '14px',
                                                                    'color': '#666',
                                                                    'margin': '0',
                                                                    'textAlign': 'left',  # 文字左对齐
                                                                    'width': '200px'
                                                                }
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                        ]
                                    ),
                                    
                                    # 综合素质模块
                                    html.Div(
                                        style={
                                            'position': 'absolute',
                                            'right': '13%',
                                            'top': '25%',  # 调整垂直位置使其落在弧形线上
                                            'zIndex': '8'
                                        },
                                        children=[
                                            # 图标和文字水平布局容器
                                            html.Div(
                                                style={
                                                    'display': 'flex',
                                                    'alignItems': 'center',
                                                    'flexDirection': 'row-reverse',  # 文字在左，图标在右
                                                    'justifyContent': 'flex-end'
                                                },
                                                children=[
                                                    # 图标容器
                                                    html.Div(
                                                        style={
                                                            'position': 'relative',
                                                            'marginLeft': '15px',  # 文字与图标之间的间距
                                                            'display': 'flex',
                                                            'alignItems': 'center',
                                                            'justifyContent': 'center'
                                                        },
                                                        children=[
                                                            # 图标背景
                                                            html.Img(
                                                                src='/assets/imgs/ico_bg.png',
                                                                style={'width': '80px', 'height': '80px'}
                                                            ),
                                                            # 图标
                                                            html.Img(
                                                                src='/assets/imgs/ico_overall.png',
                                                                style={
                                                                    'position': 'absolute',
                                                                    'width': '30px',
                                                                    'height': '30px'
                                                                }
                                                            )
                                                        ]
                                                    ),
                                                    # 文字内容容器
                                                    html.Div(
                                                        style={
                                                            'display': 'flex',
                                                            'flexDirection': 'column',
                                                            'justifyContent': 'center',
                                                            'minWidth': '200px'
                                                        },
                                                        children=[
                                                            # 标题
                                                            html.H3(
                                                                '综合素质',
                                                                style={
                                                                    'fontFamily': 'Microsoft YaHei',
                                                                    'fontSize': '16px',
                                                                    'color': '#333',
                                                                    'margin': '0 0 10px 0'
                                                                }
                                                            ),
                                                            # 描述
                                                            html.P(
                                                                '具备良好的团队协作与项目统筹能力，应对突发事件高效冷静，协调多方资源达成目标',
                                                                style={
                                                                    'fontFamily': 'Microsoft YaHei',
                                                                    'fontSize': '14px',
                                                                    'color': '#666',
                                                                    'margin': '0',
                                                                    'textAlign': 'right',  # 文字右对齐
                                                                    'width': '200px'
                                                                }
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                        ]
                                    ),
                                    
                                    # ABILITY MODULES
                                    html.Div(
                                        style={
                                            'position': 'absolute',
                                            'right': '13%',
                                            'bottom': '25%',  # 调整垂直位置使其落在弧形线上
                                            'zIndex': '8'
                                        },
                                        children=[
                                            # 图标和文字水平布局容器
                                            html.Div(
                                                style={
                                                    'display': 'flex',
                                                    'alignItems': 'center',
                                                    'flexDirection': 'row-reverse',  # 文字在左，图标在右
                                                    'justifyContent': 'flex-end'
                                                },
                                                children=[
                                                    # 图标容器
                                                    html.Div(
                                                        style={
                                                            'position': 'relative',
                                                            'marginLeft': '15px',  # 文字与图标之间的间距
                                                            'display': 'flex',
                                                            'alignItems': 'center',
                                                            'justifyContent': 'center'
                                                        },
                                                        children=[
                                                            # 图标背景
                                                            html.Img(
                                                                src='/assets/imgs/ico_bg.png',
                                                                style={'width': '80px', 'height': '80px'}
                                                            ),
                                                            # 图标
                                                            html.Img(
                                                                src='/assets/imgs/ico_innovation.png',
                                                                style={
                                                                    'position': 'absolute',
                                                                    'width': '30px',
                                                                    'height': '30px'
                                                                }
                                                            )
                                                        ]
                                                    ),
                                                    # 文字内容容器
                                                    html.Div(
                                                        style={
                                                            'display': 'flex',
                                                            'flexDirection': 'column',
                                                            'justifyContent': 'center',
                                                            'minWidth': '200px'
                                                        },
                                                        children=[
                                                            # 标题
                                                            html.H3(
                                                                '创新能力',
                                                                style={
                                                                    'fontFamily': 'Microsoft YaHei',
                                                                    'fontSize': '16px',
                                                                    'color': '#333',
                                                                    'margin': '0 0 10px 0'
                                                                }
                                                            ),
                                                            # 描述
                                                            html.P(
                                                                '积极推动智能化运维平台和体系建设，持续优化流程与工具，不断提升运维效率与服务质量',
                                                                style={
                                                                    'fontFamily': 'Microsoft YaHei',
                                                                    'fontSize': '14px',
                                                                    'color': '#666',
                                                                    'margin': '0',
                                                                    'textAlign': 'right',  # 文字右对齐
                                                                    'width': '200px'
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
                        ],
                        style={
                            'width': '100%',
                            'height': '100%',
                            'padding': '30px 80px 100px 80px'  # 调整padding，减少顶部padding使内容上移，增加底部padding为图片留出空间
                        }
                    ),

                    # 添加四张示例图片容器
                    html.Div(
                        style={
                            'position': 'absolute',
                            'bottom': '20px',  # 增加bottom值使图片整体向上移动，从20px改为100px
                            'left': '160px',
                            'right': '80px',
                            'display': 'flex',
                            'justifyContent': 'center',  # 保持居中对齐
                            'alignItems': 'center',
                            'zIndex': '7'
                        },
                        children=[
                            # example1.png
                            html.Div(
                                style={
                                    'display': 'flex',
                                    'flexDirection': 'column',
                                    'alignItems': 'center',
                                    'marginRight': '15px'  # 添加右侧margin控制间距
                                },
                                children=[
                                    html.Img(
                                        src='/assets/imgs/example1.png',
                                        style={
                                            'width': '200px',
                                            'height': '120px',
                                            'objectFit': 'contain'
                                        }
                                    )
                                ]
                            ),
                            # example2.png
                            html.Div(
                                style={
                                    'display': 'flex',
                                    'flexDirection': 'column',
                                    'alignItems': 'center',
                                    'marginRight': '15px'  # 添加右侧margin控制间距
                                },
                                children=[
                                    html.Img(
                                        src='/assets/imgs/example2.png',
                                        style={
                                            'width': '220px',
                                            'height': '130px',
                                            'objectFit': 'contain'
                                        }
                                    )
                                ]
                            ),
                            # example3.png
                            html.Div(
                                style={
                                    'display': 'flex',
                                    'flexDirection': 'column',
                                    'alignItems': 'center',
                                    'marginRight': '15px'  # 添加右侧margin控制间距
                                },
                                children=[
                                    html.Img(
                                        src='/assets/imgs/example3.png',
                                        style={
                                            'width': '200px',
                                            'height': '120px',
                                            'objectFit': 'contain'
                                        }
                                    )
                                ]
                            ),
                            # example4.png
                            html.Div(
                                style={
                                    'display': 'flex',
                                    'flexDirection': 'column',
                                    'alignItems': 'center'
                                },
                                children=[
                                    html.Img(
                                        src='/assets/imgs/example4.png',
                                        style={
                                            'width': '200px',
                                            'height': '120px',
                                            'objectFit': 'contain'
                                        }
                                    )
                                ]
                            )
                        ]
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