from dash import html
import feffery_utils_components as fuc


def render():
    """子页面：简历首页 - 面试汇报"""

    return html.Div(
        [
            # 使用FefferyDiv作为内容区域容器，添加阴影效果
            fuc.FefferyDiv(
                [
                    # 红色标题区域 - 约占2/3高度
                    html.Div(
                        [
                            html.H1(
                                '张俊的面试汇报',
                                style={
                                    'color': 'white',
                                    'textAlign': 'center',
                                    'fontSize': '64px',
                                    'fontWeight': 'bold',
                                    'margin': '0',
                                    'padding': '150px 0 30px 0',
                                    'fontFamily': '方正小标宋简体, sans-serif'  # 设置方正小标宋简体字体
                                }
                            ),
                            html.H2(
                                '2025年9月2日',
                                style={
                                    'color': 'white',
                                    'textAlign': 'center',
                                    'fontSize': '28px',
                                    'margin': '0'
                                }
                            )
                        ],
                        style={
                            'backgroundColor': '#e02020',  # 红色背景
                            'width': '100%',
                            'height': '66%',  # 占整体高度的2/3
                            'display': 'flex',
                            'flexDirection': 'column',
                            'justifyContent': 'center',
                            'alignItems': 'center'
                        }
                    ),
                    # 底部区域 - 约占1/3高度
                    html.Div(
                        [
                            html.Div(
                                [
                                    # 使用实际的zjlab.png图片
                                    html.Img(
                                        src='/assets/imgs/zjlab.png',
                                        style={
                                            'height': '200px'
                                        }
                                    ),
                                ],
                                style={
                                    'display': 'flex',
                                    'alignItems': 'center',
                                    'justifyContent': 'center',
                                    'height': '100%'
                                }
                            )
                        ],
                        style={
                            'backgroundColor': 'white',
                            'width': '100%',
                            'height': '34%',  # 占整体高度的1/3
                            'display': 'flex',
                            'flexDirection': 'column',
                            'justifyContent': 'center'
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
                    'flexDirection': 'column'
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