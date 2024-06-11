# app.py
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import requests

# Initialize the app
# Initialize the app
app = dash.Dash(__name__)
app.title = 'أنا عربيّ'

# Footer related bulk of code
footer_names = html.Div([
    html.Div([
        html.Img(src='/assets/palestine.png', style={'height': '250px'}),
    ], style={'marginLeft': '100px'}),
    html.Div([
        html.P('لينكد ان', style={'color':'#AAAAAA', 'margin': '0', 'text-align':'right'}),
        html.P('www.linkedin.com/in/mirna-maher', style={'margin': '0', 'text-align':'right'}),
        html.P('www.linkedin.com/in/nawal-shehata-77082324b', style={'margin': '0', 'text-align':'right'}),
        html.P('www.linkedin.com/in/sarah-elzahaby', style={'margin': '0', 'text-align':'right'}),
        html.P('www.linkedin.com/in/sarahh-osama', style={'margin': '0', 'text-align':'right'}),
    ], style={'display': 'flex', 'flex-direction': 'column', 'margin': '0'}),
    html.Div([
        html.P('البريد الالكتروني', style={'color':'#AAAAAA', 'margin': '0', 'text-align':'right'}),
        html.P('mirnamaher129@gmail.com', style={'margin': '0', 'text-align':'right'}),
        html.P('nwlshehata@gmail.com', style={'margin': '0', 'text-align':'right'}),
        html.P('sarahelzahaby4@gmail.com', style={'margin': '0', 'text-align':'right'}),
        html.P('sarahhosama007@gmail.com', style={'margin': '0', 'text-align':'right'}),
    ], style={'display': 'flex', 'flex-direction': 'column', 'margin': '0'}),
    html.Div([
        html.P('الاسماء', style={'color':'#AAAAAA', 'margin': '0', 'text-align':'right'}),
        html.P('ميرنا ماهر', style={'margin': '0', 'text-align':'right'}),
        html.P('نوال شحاتة', style={'margin': '0', 'text-align':'right'}),
        html.P('سارة الذهبي', style={'margin': '0', 'text-align':'right'}),
        html.P('سارة أسامة', style={'margin': '0', 'text-align':'right'}),
    ], style={'display': 'flex', 'flex-direction': 'column', 'marginRight': '100px'}),
], style={'display': 'flex', 'justify-content': 'space-between', 'width':'100%', 'marginBottom':'20px', 'margin': '0'})


# Footer content for project description
footer_description = html.Div([
html.Div([
    html.Img(src='/assets/palestine.png', style={'height': '250px'}),
], style={'marginLeft': '100px'}),
 html.P(
        'بناءً على حقيقة أن هناك العديد من البلدان التي تتحدث العربية ولكل بلد لهجته الخاصة، يهدف هذا المشروع إلى تطوير نموذج قوي يمكنه التنبؤ باللهجة المستخدمة استنادًا إلى النص المكتوب. لقد تم تحقيق دقة عالية تبلغ 85% باستخدام مزيج من النماذج التقليدية (مثل الانحدار اللوجستي ودعم المتجهات) والنماذج العميقة (مثل LSTM وGRU). يتميز النظام بإمكانية التحقق الفوري من النص المدخل، مما يتيح التعرف السريع على اللهجة. تم تصميم النموذج ليتعرف على أكثر خمس لهجات شائعة، مما يجعله أداة قيمة لعدد واسع من التطبيقات.',
           style={
            'line-height': '1.8', 
            'text-align': 'right', 
            'padding': '10px 100px 10px 100px',
            'font-size': '1em'
        }
    )], style={'display': 'flex', 'justify-content': 'space-between', 'width':'100%', 'marginBottom':'20px', 'margin': '0'})

# Pagination buttons
pagination_buttons = html.Div([
    html.Button('عنّا', id='names-button', n_clicks=0, style={ 'font-size': '1.5em', 'marginRight':'10px', 'border-radius': '20px', 'border':'none', 'background-color': '#fff', 'color':'#000', 'cursor': 'pointer'}),
    html.Button('فكرتنا', id='project-button', n_clicks=0, style={ 'font-size': '1.5em', 'marginLeft':'10px', 'border-radius': '20px', 'border':'none', 'background-color': '#fff', 'color':'#000', 'cursor': 'pointer'}),
], style={'width': '20%', 'margin': '0 auto', 'display': 'flex', 'justify-content': 'center', 'border': '1px solid #E5E5E5', 'padding': '10px', 'border-radius': '30px', 'background-color':'#E5E5E5'})
# End of Footer thing


app.layout = html.Div([
    html.Div([
        # Header (Navbar)
        html.Div([
        html.Nav([
            html.A(
                'جرّبه الآن',
                id='try-button-nav',
                href='#input-div',
                style={
                    'font-size': '20px', 
                    'padding': '8px 15px', 
                    'background-color': '#001D2F', 
                    'color': '#fff', 
                    'border': 'none', 
                    'border-radius': '5px', 
                    'cursor': 'pointer',
                    'display': 'inline-block',
                    'text-align': 'center',
                    'text-decoration': 'none'
                }),
            html.A(' الرئيسيّة', href='#', style={'padding': '15px', 'text-decoration': 'none', 'color': 'black', 'font-weight':'bold', 'font-size':'20px'}),
            html.A(' حول المشروع', href='#about-section', style={'padding': '15px', 'text-decoration': 'none', 'color': 'black', 'font-weight':'bold', 'font-size':'20px'}),
            html.A(' عنّا', href='#footer', style={'padding': '15px', 'text-decoration': 'none', 'color': 'black', 'font-weight':'bold', 'font-size':'20px'}),
        ], style={'float': 'left'}),
        html.Img(src='/assets/logo.png', style={'height': '60px'}),
    ], style={
        'display': 'flex', 
        'justify-content': 'space-between', 
        'align-items': 'center', 
        'padding': '10px 50px', 
        'background-color': '#E5E5E5',
        'position': 'fixed',
        'top': '0',
        'width': '100%',
        'z-index': '1000',
        'box-sizing': 'border-box',
        'box-shadow':'0 4px 8px rgba(0, 0, 0, 0.1)'

    }),


    # Hero Section
    html.Div([
        html.H1('سجّل.. أنا عربيّ', style={'font-size': '3.5em', 'text-align': 'center', 'margin': '20px 0'}),
        html.P('تعرّف على اللهجات العربيّة.. تحقق من لهجة نصِّكَ الآن', style={'text-align': 'center', 'font-size': '1.8em', 'margin-bottom': '30px', 'font-weight':'1em'}),
        html.Div([
               html.A(
                'جرّبه الآن',
                id='try-button',
                href='#input-div',
                style={
                    'font-size': '1.3em', 
                    'padding': '10px 20px', 
                    'background-color': '#001D2F', 
                    'color': '#fff', 
                    'border': 'none', 
                    'border-radius': '5px', 
                    'cursor': 'pointer',
                    'display': 'inline-block',
                    'text-align': 'center',
                    'text-decoration': 'none'
                })
            ])
        ], style={'height': '75vh', 
                'padding': '120px 20px', 
                'background-image': 'url("/assets/hero.jpeg")', 
                'background-size': 'cover', 
                'background-position': 'center', 
                'color': '#000',
                'display': 'flex',
                'flex-direction': 'column',
                'justify-content': 'flex-start', 
                'align-items': 'center'}),



# About Section
html.Div([
    html.Div([
        html.Div([
            html.H2('حول المشروع', style={'text-align': 'right', 'margin': '20px 0', 'color': '#000', 'font-size': '1.8em'}),
            html.P('هناك العديد من البلدان التي تتحدث العربية؛ ومع ذلك، لكل بلد لهجته الخاصة، والهدف من هذه المهمة هو بناء نموذج يتنبأ باللهجة المستخدمة استنادًا إلى النص المعطى', style={'text-align': 'right', 'color': '#000', 'font-size': '1.3em'}),
            html.Div([html.A(
                'للمزيد ',
                id='more-button',
                href='#footer',
                style={
                    'font-size': '1.3em', 
                    'padding': '10px 20px', 
                    'background-color': '#001D2F', 
                    'color': '#fff', 
                    'border': 'none', 
                    'border-radius': '5px', 
                    'cursor': 'pointer',
                    'display': 'inline-block',
                    'text-align': 'center',
                    'text-decoration': 'none',
                })], style={'margin-left':'320px'})
        ], style={'marginTop':'60px', 'marginRight':'50px', 'width':'400px'}),
        html.Div([
            html.Img(src='/assets/about_image.jpg', style={'width': '400px', 'height': '400px', 'margin': '0 auto'}),
        ], style={'text-align': 'center'})
    ], style={'text-align': 'center', 'display':'flex'})
], id='about-section', style={'padding': '50px 20px', 'background-color': '#E8EAE9', 'height':'80vh', 'display': 'flex', 'align-items': 'center', 'justify-content':'center'}),




# Features Section
html.Div([
    html.Div([
        html.Div([
            html.Img(src='/assets/feature1.png', style={'width': '50px', 'height': '50px', 'margin-top': '50px'}),
            html.H3('دقّة عالية', style={'text-align': 'center', 'color': '#fff'}),
        ], style={'padding': '20px',
                  'margin': '10px',
                  'background': 'linear-gradient(rgba(84, 103, 115, 0.3), rgba(84, 103, 115, 0.05))',
                  'border-radius': '10px',
                  'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.05)',
                  'text-align': 'center',
                  'width': '200px',
                  'height' :  '200px',
                  'flex': 'none'}),
        html.Div([
            html.Img(src='/assets/feature2.png', style={'width': '50px', 'height': '50px', 'margin-top': '50px'}),
            html.H3('التحقق الوقتي من النص', style={'text-align': 'center', 'color': '#fff'}),
        ], style={'padding': '20px',
                  'margin': '10px',
                  'background': 'linear-gradient(rgba(84, 103, 115, 0.3), rgba(84, 103, 115, 0.05))',
                  'border-radius': '10px',
                  'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.05)',
                  'text-align': 'center',
                  'width': '200px',
                  'height' :  '200px',
                  'flex': 'none'}),
        html.Div([
            html.Img(src='/assets/feature3.png', style={'width': '50px', 'height': '50px', 'margin-top': '50px'}),
            html.H3('التعرف على أكثر خمس لهجات شائعة', style={'text-align': 'center', 'color': '#fff'}),
        ], style={'padding': '20px',
                  'margin': '10px',
                  'background': 'linear-gradient(rgba(84, 103, 115, 0.3), rgba(84, 103, 115, 0.05))',
                  'border-radius': '10px',
                  'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.05)',
                  'text-align': 'center',
                  'width': '200px',
                  'height' :  '200px',
                  'flex': 'none'}),
        html.Div([
            html.Img(src='/assets/feature4.png', style={'width': '50px', 'height': '50px', 'margin-top': '50px'}),
            html.H3('سهولة الاستخدام', style={'text-align': 'center', 'color': '#fff'}),
        ], style={'padding': '20px',
                  'margin': '10px',
                  'background': 'linear-gradient(rgba(84, 103, 115, 0.3), rgba(84, 103, 115, 0.05))',
                  'border-radius': '10px',
                  'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.05)',
                  'text-align': 'center',
                  'width': '200px',
                  'height' :  '200px',
                  'flex': 'none',
                  }),
        html.Div([
            html.Div([
                html.Img(src='/assets/sparkles.png', style={'width': '30px', 'height': '30px', 'margin-top':'20px'}),
                html.H1('المميزات', style={'text-align': 'right', 'color': '#fff', 'font-size': '2em'})
                ], style={'display': 'flex', 'justify-content': 'space-around'}),

            html.P('لماذا نحن اختياركم الأول؟', style={'text-align': 'right', 'color': '#fff', 'margin-right': '20px', 'font-size': '1.3em'}),
            ], style={'padding': '20px',
                    'margin': '10px',
                    'text-align': 'center',
                    'width': '200px',
                    'height' :  '200px',
                    'flex': 'none'}),
    ], style={'display': 'flex', 'justify-content': 'space-around'})
], style={'padding': '50px 20px', 'background-color': '#001D2F', 'height':'30vh'}),


    # Input Section
    html.Div([
        html.Div([
            html.Fieldset([
                html.Legend('ادخل هُنا النص المُراد التعرف عليه', style={'color': '#001D2F', 'font-size':'1.3em'}),
                dcc.Textarea(
                    id='input-text',
                    style={
                        'width': '100%',
                        'height': '150px',
                        'border': 'none',
                        'outline': '0',
                        'resize': 'none',
                        'background-color': '#E8EAE9',
                        'font-size': '1.5em'
                    }
                ),
            ], style={'border': '1px solid #001D2F', 'border-radius': '5px', 'padding': '10px', 'width': '1000px'})
        ]),

        html.Div([
               html.Button(
                'احذف النص',
                id='remove-button',
                style={
                    'font-size': '1em',
                    'padding': '10px 20px',
                    'background-color': '#6E0F11',
                    'color': '#fff',
                    'border': 'none',
                    'border-radius': '5px',
                    'cursor': 'pointer',
                    'font-weight':'bold'
                }
            ),
            html.Button(
                'حلّل النص',
                id='analyze-button',
                style={
                    'font-size': '1em',
                    'padding': '10px 20px',
                    'background-color': '#001D2F',
                    'color': '#fff',
                    'border': 'none',
                    'border-radius': '5px',
                    'cursor': 'pointer',
                    'margin-left': '10px', 
                    'font-weight':'bold'
                }
            )
        ], style={'display': 'flex', 'justify-content': 'center', 'margin-top': '20px'})
], id='input-div', style={'padding': '20px', 'background-color': '#E8EAE9', 'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'marginTop':'50px'}),



    # Results Section
    html.Div([
        html.H2('النتائج', style={'text-align': 'center', 'margin': '20px 0'}),
        html.Div(id='results-output', style={'text-align': 'center', 'font-size': '1.2em', 'margin-top': '20px'})
    ], style={'padding': '50px 20px', 'background-color': '#E8EAE9'})
    ], style={'background-color': '#E8EAE9', 'align-items':'center'}),

# Footer
html.Footer([
    html.Div([
        footer_names,
    ], id='footer', style={'height':'150px'}),
    html.Div([
        pagination_buttons  
    ])
], style={'padding': '50px 50px', 'background-color': '#001D2F', 'color': '#fff', 'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-between'}),
html.Div([
    html.P('حقوق النشر محفوظة @ 2024') 
], style={'text-align':'center', 'background-color': '#00131F', 'align-items':'center', 'color':'white', 'height':'3vh', 'justify-content':'center', 'align-items':'center'})

], style={'background-color':'#001D2F'})


# Callback to switch between pages
@app.callback(
    Output('footer', 'children'),
    [Input('names-button', 'n_clicks'), Input('project-button', 'n_clicks'), Input('more-button', 'n_clicks')]
)
def update_footer(names_clicks, project_clicks, more_clicks):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'names-button' in changed_id:
        return footer_names
    elif 'project-button' in changed_id:
        return footer_description
    elif 'more-button' in changed_id:
        return footer_description
    else:
        return footer_names
    
# Callback to update pagination buttons
@app.callback(
    Output('names-button', 'style'),
    Output('project-button', 'style'),
    [Input('names-button', 'n_clicks'), Input('project-button', 'n_clicks'), Input('more-button', 'n_clicks')]
)
def update_button_style(names_clicks, project_clicks, more_clicks):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    names_style = {'font-size': '1em', 'border-radius': '20px', 'border': 'none', 'background-color': '#001D2F', 'color': '#E8EAE9', 'cursor': 'pointer', 'width':'40%', 'height':'30px'}
    project_style = {'font-size': '1em', 'border-radius': '20px', 'border': 'none', 'background-color': '#E8EAE9', 'color': '#001D2F', 'cursor': 'pointer', 'width':'40%', 'height':'30px'}

    if button_id == 'names-button':
        names_style['background-color'] = '#001D2F'
        names_style['color'] = '#E5E5E5'
        project_style['background-color'] = '#E5E5E5'
        project_style['color'] = '#001D2F'
    elif button_id == 'project-button' or button_id == 'more-button':
        project_style['background-color'] = '#001D2F'
        project_style['color'] = '#E5E5E5'
        names_style['background-color'] = '#E5E5E5'
        names_style['color'] = '#001D2F'

    return names_style, project_style


@app.callback(
    Output('input-text', 'value'),
    [Input('remove-button', 'n_clicks')]
)
def clear_text_area(n_clicks):
    if n_clicks:
        return '' 
    else:
        return dash.no_update


@app.callback(
    Output('results-output', 'children'),
    [Input('analyze-button', 'n_clicks')],
    [State('input-text', 'value')]
)
def analyze_text(n_clicks, input_text):
    print(f"Button clicked {n_clicks} times")
    if n_clicks > 0 and input_text:
        print(f"Input text: {input_text}")
        response = requests.post('http://localhost:5000/predict', json={'text': input_text})
        print(f"Server response status: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Predicted label: {result['predicted_label']}")
            if result["predicted_label"] == 'LB':
                return html.Div([
                    html.P('اللبنانيّة', style={'fontSize': '2em', 'color': '#001D2F', 'padding':'20px 20px 0 0'}),
                    html.Img(src='/assets/LB.png', style={'width': '50px', 'height': '50px', 'margin-top': '50px'})
                ], style={'textAlign': 'center', 'display':'flex', 'justify-content':'center'})
            elif result["predicted_label"] == 'EG':
                return html.Div([
                    html.P('المصريّة', style={'fontSize': '2em', 'color': '#001D2F', 'padding':'20px 20px 0 0'}),
                    html.Img(src='/assets/EG.png', style={'width': '50px', 'height': '50px', 'margin-top': '50px'})
                ], style={'textAlign': 'center', 'display':'flex', 'justify-content':'center'})
            elif result["predicted_label"] == 'LY':
                return html.Div([
                    html.P('الليبيّة', style={'fontSize': '2em', 'color': '#001D2F', 'padding':'20px 20px 0 0'}),
                    html.Img(src='/assets/LY.png', style={'width': '50px', 'height': '50px', 'margin-top': '50px'})
                ], style={'textAlign': 'center', 'display':'flex', 'justify-content':'center'})
            elif result["predicted_label"] == 'SD':
                return html.Div([
                    html.P('السودانيّة', style={'fontSize': '2em', 'color': '#001D2F', 'padding':'20px 20px 0 0'}),
                    html.Img(src='/assets/SD.png', style={'width': '50px', 'height': '50px', 'margin-top': '50px'})
                ], style={'textAlign': 'center', 'display':'flex', 'justify-content':'center'})
            elif result["predicted_label"] == 'MA':
                return html.Div([
                    html.P('المغربيّة', style={'fontSize': '2em', 'color': '#001D2F', 'padding':'20px 20px 0 0'}),
                    html.Img(src='/assets/MA.png', style={'width': '50px', 'height': '50px', 'margin-top': '50px'})
                ], style={'textAlign': 'center', 'display':'flex', 'justify-content':'center'})
        else:
            print("Error: Could not process the request.")
            return html.Div([
                html.H3('Error:'),
                html.P('Could not process the request.', style={'fontSize': '2em', 'color': 'red'})
            ], style={'textAlign': 'center'})
    return html.Div('')

# Run the app
if __name__ == '__main__':
    app.run_server(port=8051, jupyter_mode='external')