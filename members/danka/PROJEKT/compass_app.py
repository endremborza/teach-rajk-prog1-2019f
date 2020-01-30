import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import json
import glob
import pandas as pd
import base64

with open("questions_in_lines.txt", "r", encoding="utf-8") as fp:
    questionlist = fp.read().split("\n")

questions = []
for i in range(0, len(questionlist)):
    questions.append(html.H6(style={'margin-bottom': 10}, children=questionlist[i]))
    questions.append(html.Div(style={'margin-bottom': 80}, children=dcc.Slider(
        id='slider' + str(i),
        min=0,
        max=4,
        included=False,

        marks={
            0: {'label': 'Még nem válaszoltam'},
            1: {'label': 'Nagyon nem értek egyet'},
            2: {'label': 'Nem értek egyet'},
            3: {'label': 'Egyetértek'},
            4: {'label': 'Nagyon egyetértek'},
        },
    )
                              ))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'margin-left': 250, 'margin-right': 250, 'margin-top': 50}, children=[
    html.H1(children='CollegeCompass 1.0'),

    html.Div(style={'margin-bottom': 50, 'text-align': 'justify'}, children='''
        Ez itt a rajkos political compass első verziója. 
        Kérlek jelöld be, hogy mennyire értesz egyet a lenti állításokkal, így megtudhatod 
        hol helyezkedsz el a Rajkos political compass tengelyein. Az állítások sosem személyesen rád vonatkoznak; 
        inkább arra, hogy mit gondolsz, hogyan működik/kellene, hogy működjön a kollégium egésze, mint szervezet.
    '''),

    html.Div(children=questions),

    html.Div(id='output-container-button', style={'margin-bottom': 10},
             children='Add meg a teljes neved, kattints, tekerj le és nézd meg az eredményt!'),
    html.Div(style={'margin-bottom': 30}, children=dcc.Input(id='input-box', type='text')),
    html.Div(style={'margin-bottom': 60}, children=html.Button('Mutasd az eredményt', id='button')),

    html.Div(id='compassgraph'),
    html.Div(id='desctitle'),
    html.Div(id='desctext')
])


@app.callback(
    Output('compassgraph', 'children'),
    [Input('button', 'n_clicks')] +
    [Input('input-box', 'value')] +
    [Input('slider%d' % i, 'value') for i in range(len(questionlist))])
def update_result(*args):
    name = args[1]
    if all(arg is not None for arg in args) and all(arg is not 0 for arg in args):
        answer_record = {
            "név": name
        }
        for qid, q in enumerate(questionlist):
            answer_record[q] = args[qid + 2]
        json.dump(answer_record, open("answers/answer_{}.json".format(name), "w"))
        json_files = glob.glob("answers/*.json")
        list_of_dicts = []
        for f in json_files:
            list_of_dicts.append(json.load(open(f)))
        # answer_df = pd.DataFrame(list_of_dicts)
        q_categ_df = pd.read_excel('questions.xlsx', header=0, encoding='utf-8', sheet_name="questions")

        q_categ_df["kérdés"] = q_categ_df["kérdés"].map(lambda x: x.strip())

        answer_dict = next(item for item in list_of_dicts if item["név"] == name)

        result_dict = {
            "yscore": 0,
            "xscore": 0
        }

        for q in answer_dict:  # qeustions_ansered:
            axis = 0
            for k in result_dict.keys():  # tengelys:
                if getattr(q_categ_df, 'kérdés').isin([q]).any():
                    sign = q_categ_df.loc[lambda df: df[q_categ_df.columns[0]] == q][
                        q_categ_df.columns[1:].tolist()].values.tolist()[0]
                    # oszlopban
                    if sign[axis] == '-':
                        if answer_dict.get(q) == 1:
                            result_dict[k] += 2
                        if answer_dict.get(q) == 2:
                            result_dict[k] += 1
                        if answer_dict.get(q) == 3:
                            result_dict[k] -= 1
                        if answer_dict.get(q) == 4:
                            result_dict[k] -= 2
                    if sign[axis] == '+':
                        if answer_dict.get(q) == 1:
                            result_dict[k] -= 2
                        if answer_dict.get(q) == 2:
                            result_dict[k] -= 1
                        if answer_dict.get(q) == 3:
                            result_dict[k] += 1
                        if answer_dict.get(q) == 4:
                            result_dict[k] += 2
                    axis += 1

        xscore = result_dict["xscore"]
        yscore = result_dict["yscore"]

        print(xscore)
        print(yscore)

        ########################################################################################################

        desc = [dcc.Graph(
            style={'height': 600},
            id='compassgraph',
            figure=go.Figure(
                data=[
                    go.Scatter(
                        x=[xscore],
                        y=[yscore],
                        text=name,
                        mode='text',
                    )
                ],
                layout=go.Layout(
                    clickmode='none',
                    dragmode=False,

                    title='Rajk College Compass',
                    margin=dict(l=40, r=0, t=40, b=30),
                    xaxis=dict(type="linear",
                               range=[-50, 50],
                               title="Belső - Külső orientáltság",
                               autorange=False),
                    yaxis=dict(type="linear",
                               range=[-50, 50],
                               title="Stabilitás, kontroll - Rugalmasság dinamizmus",
                               autorange=False),
                    paper_bgcolor='rgba(0,0,0,0)',
                    images=[dict(
                        source="http://bespokeprinciples.com/wp-content/uploads/2016/08/21-705x591.jpg",
                        xref="paper", yref="paper",
                        x=0.5, y=0.5,
                        sizex=0.5, sizey=0.5,
                        xanchor="center",
                        yanchor="middle",
                        sizing="stretch",
                        layer="above")]
                )
            )
        )]

        if xscore == 0 or yscore == 0:
            desc.append(html.Div(style={'margin-bottom': 50, 'margin-top': 40},
                                 children='''Hűha! A Te nézeteid pont a határon vannak.'''))

        if xscore <= 0 and yscore >= 0:
            desc.append(html.H1(style={'margin-top': 40}, children='Klán', id='desctitle'))

            image_filename = r'C:\Users\tatai\Documents\PROG\PROJEKT\flat-vector-klan.jpg'
            encoded_image = base64.b64encode(open(image_filename, 'rb').read())

            desc.append(html.Div(style={'margin-bottom': 50, 'margin-right': 90, 'margin-top': -20, 'width': '30%',
                                        'display': 'inline-block'}, id='image',
                                 children=[html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))]))

            desc.append(html.Div(style={'margin-bottom': 50, 'width': '55%', 'display': 'inline-block',
                                        'text-align': 'justify'}, id='desctext', children='''A kollégiumról való 
            elképzeléseid egy klánhoz állnak legközelebb. Elsősorban egyénekben és csapatokban gondolkozol, 
            a Rajk belső ügyei jobban érdekelnek, mint a külvilágra gyakorolt hatás, vagy a külvilágban rólunk látott 
            kép. A kollégiumi vezetőktől a támogatást, mentorálást, a csapatra való figyelmet várod leginkább. Hiszel 
            az információk minél nagyobb fokú megosztásában, az emberek döntési folyamatokba való bevonásában, 
            az egyéni fejlődés erejében és abban, hogy itt bárki bármit csinálhat – szerinted ezek az elemek 
            alakítják ki az összetartás érzését a Rajkban.'''))

        if xscore <= 0 and yscore <= 0:
            desc.append(html.H1(style={'margin-top': 40}, children='Hierarchia', id='desctitle'))

            image_filename = r'C:\Users\tatai\Documents\PROG\PROJEKT\flat-vector-hierarchia.jpg'
            encoded_image = base64.b64encode(open(image_filename, 'rb').read())

            desc.append(html.Div(style={'margin-bottom': 50, 'margin-right': 90, 'margin-top': -20, 'width': '30%',
                                        'display': 'inline-block'}, id='image',
                                 children=[html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))]))

            desc.append(html.Div(style={'margin-bottom': 50, 'width': '55%', 'display': 'inline-block',
                                        'text-align': 'justify'}, id='desctext', children='''A Rajkot sok szempontból egy 
            hierarchikus rendszerként látod, ahol a folyamatok koordináltságán, szervezettségén van a hangsúly. 
            Fontosak számodra a közösség lefektetett szabályai, az azokhoz való ragaszkodás, ezek adják meg a rajkos 
            kultúra alapját. Hiszel abban, hogy a rendszereket és az embereket is érdemes szoros kontroll alatt 
            tartani, amelyekre elsősorban a kialakított pozíciók és a hozzájuk kapcsolódó döntési jogkörök alkalmas. 
            A rajkos vezetőktől is éppen ezért koordináló, szervező, felügyelő szerepet vársz el. A kollégium neked 
            elsősorban a belső folyamatainkról, a problémák megoldásáról, és saját eredményességünkről szól.'''))

        if xscore >= 0 and yscore >= 0:
            desc.append(html.H1(style={'margin-top': 40}, children='Adhokrácia', id='desctitle'))
            desc.append(html.Div(style={'margin-bottom': 50, 'width': '65%', 'display': 'inline-block',
                                        'text-align': 'justify'}, id='desctext', children='''A kollégiumról alkotott 
            elképzeléseid leginkább egy adhokráciához hasonlítanak. Fontosnak tartod, hogy a Rajk a külvilágban 
            érvényes sztenderdeknek megfeleljen, az intézmény tevékenységeinek orientációjában nagy szerepet szánsz a 
            külső hatásnak. Néha torkig vagy a folyamatos köldöknézegetéssel. Nagy hangsúlyt fektetsz a kollégium 
            folyamatos változására, szereted az új, innovatív ötleteket, alulról jövő kezdeményezéseket. A kollégiumi 
            vezetőktől is vállalkozó szellemet, bátorságot, víziót vársz. Számodra a kollégium egy folyamatosan 
            változó hely, amelyet az tart össze, hogy kreatív energiánkkal újra és újra átalakítjuk.'''))

            image_filename = r'C:\Users\tatai\Documents\PROG\PROJEKT\flat-vector-adhokracia.jpg'
            encoded_image = base64.b64encode(open(image_filename, 'rb').read())

            desc.append(html.Div(style={'margin-bottom': 50, 'margin-left': 20, 'margin-top': -20, 'width': '30%',
                                        'display': 'inline-block'}, id='image',
                                 children=[html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))]))

        if xscore >= 0 and yscore <= 0:
            desc.append(html.H1(style={'margin-top': 40}, children='Piac', id='desctitle'))
            desc.append(html.Div(style={'margin-bottom': 50, 'width': '55%',
                                        'display': 'inline-block', 'text-align': 'justify'}, id='desctext', children=
                                 '''A Rajkot egy célorientált kulturális közegként látod. A verseny jelen van mind a 
                                 kollégium falain belül, mind azon kívül, az ebben való helytálláshoz precíz 
                                 tervezésre, a célok felsőbb szintű meghatározására van szükség. A 
                                 teljesítményorientáltságot a kollégium egyik – ha nem a – legfontosabb értékének 
                                 tartod. A vezetőknek ebből fakadóan szintén keménykezűnek kell lenniük, hogy ezt a 
                                 hangulatot kialakítsák. Úgy látod, hogy a kollégiumnak minél több külső partnerre 
                                 van szüksége, hogy tartani tudja a tempót a versenytársaival. Összességében a 
                                 kollégium számodra a barátságos versengés helye, ahol ezzel egymást is felfelé 
                                 húzzuk, de hasonlóan fontosnak látod, hogy koordináltan reagáljunk a külső 
                                 kihívásokra is, és ott is versenyben maradjunk.'''))

            image_filename = r'C:\Users\tatai\Documents\PROG\PROJEKT\flat-vector-piac.jpg'
            encoded_image = base64.b64encode(open(image_filename, 'rb').read())

            desc.append(html.Div(style={'margin-bottom': 20, 'margin-left': 20, 'margin-top': -40, 'width': '30%',
                                        'display': 'inline-block'}, id='image',
                                 children=[html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))]))

        return desc


if __name__ == '__main__':
    app.run_server(debug=True, host='146.110.61.227')
