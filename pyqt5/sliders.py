#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scrollbars are used for viewing documents or images that are larger than the view area.
To display horizontal or vertical scrollbars, you use the HorizontalScrollBar and VerticalScrollBar widgets,
which are instances of the QScrollBar class.
These scrollbars have a slider handle that can be moved to view the area that is not visible.
The location of the slider handle indicates the location within the document or image.

[*] Scrollbar has the following controls:
    - Slider handle: This control is used to move to any part of the document or image quickly.
    - Scroll arrows: These are the arrows on either side of the scrollbars that are used to view the desired area of the document
                     or image that is not currently visible.
                     On using these scroll arrows, the position of the slider handle moves to show the current location within the
                     document or image.
    - Page control: The page control is the background of the scrollbar over which the slider handle is dragged.
                    When the background is clicked, the slider handle moves towards the click by one page.
                    The amount the slider handle moves can be specified via the pageStep property.
                    The page step is the amount by which a slider moves when the user presses the Page Up and Page Down keys.
                    You can set the amount of the pageStep property by using the setPageStep() method.


[*] The method that is specifically used to set and retrieve values from scrollbars is the value() method, described here.
    The value() method fetches the value of the slider handle, that is, its distance value from the start of the scrollbar.
    You get the minimum value of the scrollbar when the slider handle is at the top edge in a vertical scrollbar or at the
    left edge in a horizontal scrollbar, and you get the maximum value of the scroll bar when the slider handle is at the bottom
    edge in a vertical scrollbar or at the right edge in a horizontal scrollbar.
    You can move the slider handle to its minimum and maximum values via the keyboard too, by pressing the Home and End keys,
    respectively. Let's take a look at the following methods:
    - setValue(): This method assigns value to the scrollbar and, as per the value
    - assigned, the location of the slider handle is set in the scrollbar
    - minimum(): This method returns the minimum value of the scrollbar
    - maximum(): This method returns the maximum value of the scrollbar
    - setMinimum(): This method assigns the minimum value to the scrollbar
    - setMaximum(): This method assigns the maximum value to the scrollbar
    - setSingleStep(): This method sets the single step value
    - setPageStep(): This method sets the page step value
[NB] QScrollBar provides only integer values.

[*] The signals emitted through the QScrollBar class are shown in the following list:
    - valueChanged(): This signal is emitted when the scrollbar's value is changed, that is, when its slider handle is moved
    - sliderPressed(): This signal is emitted when the user starts to drag the slider handle
    - sliderMoved(): This signal is emitted when the user drags the slider handle
    - sliderReleased(): This signal is emitted when the user releases the slider handle
    - actionTriggered(): This signal is emitted when the scrollbar is changed by user interaction
"""

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from headers.demoSliders import *


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.horizontalScrollBarSugarLevel.valueChanged.connect(self.scroll_horizontal)
        self.ui.verticalScrollBarPulseRate.valueChanged.connect(self.scroll_vertical)
        self.ui.horizontalSliderBloodPressure.valueChanged.connect(self.slider_horizontal)
        self.ui.verticalSliderCholestrolLevel.valueChanged.connect(self.slider_vertical)

        self.show()

    def scroll_horizontal(self, value):
        self.ui.lineEditResult.setText('Sugar Level: {}'.format(value))

    def scroll_vertical(self, value):
        self.ui.lineEditResult.setText('Pulse Rate: {}'.format(value))

    def slider_horizontal(self, value):
        self.ui.lineEditResult.setText('Blood Pressure: {}'.format(value))

    def slider_vertical(self, value):
        self.ui.lineEditResult.setText('Cholestrol Level: {}'.format(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
