from dash import html
import feffery_utils_components as fuc

def render():
    """子页面：简历结尾 - 感谢页面"""

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
                    
                    # 顶部空白区域
                    html.Div(
                        style={
                            'width': '100%',
                            'height': '150px',  # 控制顶部空白高度
                            'backgroundColor': 'transparent'  # 透明背景
                        }
                    ),
                    
                    # 红色感谢区域 - 约占40%高度
                    html.Div(
                        [
                            html.H1(
                                '谢谢',
                                style={
                                    'color': 'white',
                                    'textAlign': 'center',
                                    'fontSize': '120px',
                                    'fontWeight': 'bold',
                                    'margin': '0',
                                    'padding': '0',
                                    'lineHeight': '1'
                                }
                            )
                        ],
                        style={
                            'backgroundColor': '#e02020',  # 红色背景
                            'width': '100%',
                            'height': 'calc(40% - 50px)',  # 调整高度以适应整体布局
                            'display': 'flex',
                            'flexDirection': 'column',
                            'justifyContent': 'center',
                            'alignItems': 'center'
                        }
                    ),
                    
                    # 底部图片区域
                    html.Div(
                        [
                            # 使用pic_end.png图片
                            html.Img(
                                src='/assets/imgs/pic_end.png',
                                style={
                                    'width': '100%',
                                    'height': '100%',
                                    'objectFit': 'cover'
                                }
                            )
                        ],
                        style={
                            'width': '100%',
                            'height': '50%',  # 保持底部图片区域高度
                            'overflow': 'hidden'
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
                    'flexDirection': 'column',
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
            #'backgroundColor': '#f0f0f0',  # 整体页面灰色背景
            'backgroundColor': '#ffffff',  # 修改为白色背景
            'boxSizing': 'border-box',
            'display': 'flex',
            'alignItems': 'center',
            'justifyContent': 'center'
        }
    )