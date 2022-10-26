from turtle import color

# to import PySimpleGUI
import PySimpleGUI as sg

# to import the classes
from Blackboard import Blackboard
from FrequencyKS import FrequencyKS
from SentimentAnalysisKS import SentimentAnalysisKS
from SpellingCheckerKS import SpellingCheckerKS
from GrammarCheckerKS import GrammarCheckerKS
from Controller import Controller

# Import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# to draw the canvas that holds the bar chart
def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

if __name__ == "__main__":

    # GUI window theme
    sg.theme('Dark Brown 1') 

    # to define fields on the left column
    left_column = [
        [
            sg.Text('Input: '), sg.Input(size=(41, 1), 
            key='-input-file-', enable_events=True),  
            sg.FileBrowse(key='-button-file-', 
            file_types=(("Text Files", "*.txt"),))
            ],
        [
            sg.Multiline('', key='-multiline-text-', size=(55,30))
            ],
        [
            sg.Button('START', pad=(170, 0))
            ],
    ]

    # to define fields on the right column
    right_column = [
        [
        sg.Text('Changes: ', pad=(20, 0)), 
        sg.Multiline('', key='-multiline-changes-', size=(55,3), autoscroll=True,pad=((0,0),(0,10)))
            ],
            [sg.HSeparator()],
            [sg.Text('Frequency',pad=((250,0),(10,15)), justification='center',font="bold")],
            [
                sg.Text("Character Frequency: "), sg.Input(readonly=True, size=(8, 1), key='-char-freq-text-', text_color="black"),
                sg.Text("Word Frequency: "), sg.Input(readonly=True, size=(8, 1), key='-word-freq-text-',text_color="black"),
                sg.Text("Sentence Frequency: "), sg.Input(readonly=True, size=(8, 1), key='-sentence-freq-text-',text_color="black"),
            ],
            [sg.HSeparator(pad=(0,15))],
            [sg.Text('Sentiment Analysis',pad=((225,0),(0,10)), justification='center',font="bold")],
            [sg.Canvas(key='-CANVAS-')],

    ]


    # to define the layout of the GUI
    layout = [
        [sg.Column(left_column),
        sg.VSeperator(),
        sg.Column(right_column),]
    ]


    window = sg.Window('Blackboard Pattern-Based Text Analyzer', layout, margins=(20, 20), finalize=True)
    window['-multiline-text-'].update(disabled=True)


    while True:  # Event Loop
        event, values = window.read()

        if(event == '-input-file-'):
            # to read the text file
            file = open(values['-input-file-'],"r")
            text = file.read()
            window['-multiline-text-'].update(text)

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'START':
            if  values['-input-file-'] == '':
                # error handling - in case no file is chosen
                sg.popup("No filename chosen! Please choose a file to be analyzed!")
            else:
                window['START'].update(disabled=True)

                # to read the text file
                file = open(values['-input-file-'],"r")
                text = file.read()

                # to create an instance of blackboard
                blackboard = Blackboard(text)

                # to display the initial text
                window['-multiline-text-'].update(blackboard.getText())

                 # Close the file stream
                file.close()

                # register the knowledge sources with the blackboard
                # Send multilinetext change
                changeText = window['-multiline-changes-']
                changeBlackboard = window['-multiline-text-']
                blackboard.registerKnowledgeSource(SpellingCheckerKS(blackboard))
                blackboard.registerKnowledgeSource(GrammarCheckerKS(blackboard))
                blackboard.registerKnowledgeSource(FrequencyKS(blackboard))
                blackboard.registerKnowledgeSource(SentimentAnalysisKS(blackboard))

                # When loading the text set the state of the blackboard to changed
                blackboard.state = 'changed'


                # Start the controller that starts all the knowledge sources
                controller = Controller(blackboard)
                controller.startController()
                
                # to update the text area with the final blackboard value
                window['-multiline-text-'].update(blackboard.getText())

                # error handling - these fields are disabled to avoid user from making mistakes
                window['-input-file-'].update(disabled=True)
                window['-button-file-'].update(disabled=True)
                window['-multiline-changes-'].update(disabled=True)

                # Intialisation of Bar Chart from matplotlib
                sentiment = controller.sentiments
                # creating the dataset
                data = {
                    'Positive Sentiment':sentiment[0], 
                    'Negative Sentiment':sentiment[1]
                }
                xAxis = list(data.keys())
                yAxis = list(data.values())
                fig = plt.figure(figsize=(6,4))
                # creating the bar plot
                plt.bar(xAxis, yAxis, width = 0.4, color="blue")
                # plt.xlabel("Sentiment")
                plt.ylabel("Sentiment")

                # uodate the GUI with the values
                fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
                window['-char-freq-text-'].update(controller.frequency[0])
                window['-word-freq-text-'].update(controller.frequency[1])
                window['-sentence-freq-text-'].update(controller.frequency[2])
                window['-multiline-changes-'].update(controller.trace)

                # to output the final blackboard value into a text file
                fileOutput = open(values['-input-file-'][:-4] + "-analyzed.txt","w")
                fileOutput.write(blackboard.getText())
                fileOutput.close()

    window.close()
    
    