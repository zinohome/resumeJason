from dash import html
import feffery_utils_components as fuc


def render():
    """子页面：简历日程 - Agenda"""

    return html.Div(
        [
            # 使用FefferyDiv作为内容区域容器，添加阴影效果
            fuc.FefferyDiv(
                [
                    # 右上角logo和文字
                    html.Div(
                        [
                            html.A(
                                href='/core/cvhome',
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
                    
                    # 主内容区域 - 分为左侧提纲区域和右侧图片区域
                    html.Div(
                        [
                            # 左侧介绍提纲内容（包含红色竖条和文本）
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
                                    
                                    # 介绍提纲标题
                                    html.H1(
                                        '介绍提纲',
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
                                    'marginBottom': '80px'
                                }
                            ),
                            
                            # 左侧提纲条目和右侧图片并排显示
                            html.Div(
                                [
                                    # 提纲条目列表
                                    html.Div(
                                        [
                                            html.A(
                                                '一、基本情况介绍',
                                                href='/core/cvinfo',
                                                target='_self',
                                                style={
                                                    'fontSize': '28px',
                                                    'color': '#333',
                                                    'margin': '0 0 40px 0',
                                                    'textDecoration': 'none'  # 可根据需要保留或去除下划线
                                                }
                                            ),
                                            html.A(
                                                '二、主要工作业绩',
                                                href='/core/cvwork',
                                                target='_self',
                                                style={
                                                    'fontSize': '28px',
                                                    'color': '#333',
                                                    'margin': '0 0 40px 0',
                                                    'textDecoration': 'none'
                                                }
                                            ),
                                            html.A(
                                                '三、个人优势',
                                                href='/core/cvcharact',
                                                target='_self',
                                                style={
                                                    'fontSize': '28px',
                                                    'color': '#333',
                                                    'margin': '0 0 40px 0',
                                                    'textDecoration': 'none'
                                                }
                                            ),
                                            html.A(
                                                '四、未来工作规划',
                                                href='/core/cvplan',
                                                target='_self',
                                                style={
                                                    'fontSize': '28px',
                                                    'color': '#333',
                                                    'margin': '0',
                                                    'textDecoration': 'none'
                                                }
                                            )
                                        ],
                                        style={
                                            'flex': '1',
                                            'display': 'flex',
                                            'flexDirection': 'column',
                                            'justifyContent': 'flex-start'
                                        }
                                    ),
                                    
                                    # 右侧图片区域 - 显示zjlab-stone.png
                                    html.Div(
                                        html.Img(
                                            src='/assets/imgs/zjlab-stone.png',
                                            style={
                                                'width': '100%',
                                                'height': '100%',
                                                'objectFit': 'contain'  # 保持图片比例
                                            }
                                        ),
                                        style={
                                            'flex': '1.2',  # 图片区域稍宽
                                            'height': '400px',
                                            'overflow': 'hidden',
                                            'display': 'flex',
                                            'alignItems': 'center',
                                            'justifyContent': 'center',
                                            'marginLeft': '60px'
                                        }
                                    )
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