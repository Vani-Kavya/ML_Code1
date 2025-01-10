{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "49d50428-95f2-432f-90b9-4ba5e2118b81",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pickle\n",
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "cb9330a2-474a-4395-b537-3c135b12b181",
   "metadata": {},
   "outputs": [],
   "source": [
    "loaded_model = pickle.load(open('trained_model_Latptop_Price_Prediction.sav', 'rb'))\n",
    "df = pickle.load(open('df.sav','rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a19397d6-af35-4ab1-b81c-7a95e7c20d6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Laptop_Price_Prediction_function(input_data):\n",
    "    \n",
    "\n",
    "# changing the input_data to numpy array\n",
    "    input_data_as_numpy_array = np.asarray(input_data)\n",
    "\n",
    "# reshape the array as we are predicting for one instance\n",
    "    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)\n",
    "\n",
    "    prediction = loaded_model.predict(input_data_reshaped)\n",
    "    print(\"Laptop_Price_Prediction (As_Per_Given_Configuration) : \", round(np.exp(prediction[0]),2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b7013565-6c53-4a68-a66f-1ae39a0229d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-10 15:35:08.221 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Vanita\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "def main():\n",
    "    st.title(\"Laptop Price Prediction Web App\")\n",
    "\n",
    "\n",
    "    Company = st.selectbox('Brand',df['Company'].unique())\n",
    "    TypeName = st.selectbox('Type',df['TypeName'].unique())\n",
    "    Ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])\n",
    "    Weight = st.number_input('Weight of the Laptop')\n",
    "    Touchscreen = st.selectbox('Touchscreen',['No','Yes'])\n",
    "    Ips = st.selectbox('IPS',['No','Yes'])\n",
    "    Screen_size = st.slider('Scrensize in inches', 10.0, 18.0, 13.0)\n",
    "    Resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])\n",
    "    CPU = st.selectbox('CPU',df['Cpu brand'].unique())\n",
    "    HDD = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])\n",
    "    SSD = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])\n",
    "    GPU = st.selectbox('GPU',df['Gpu brand'].unique())\n",
    "    OS = st.selectbox('OS',df['os'].unique())\n",
    "\n",
    "\n",
    "    Prediction=\"\"\n",
    "    if st.button(\"Predict_Price: \"):\n",
    "        # query\n",
    "        ppi = None\n",
    "        if Touchscreen == 'Yes':\n",
    "            Touchscreen = 1\n",
    "        else:\n",
    "            Touchscreen = 0\n",
    "\n",
    "        if Ips == 'Yes':\n",
    "            Ips = 1\n",
    "        else:\n",
    "            Ips = 0\n",
    "\n",
    "        X_res = int(resolution.split('x')[0])\n",
    "        Y_res = int(resolution.split('x')[1])\n",
    "        ppi = ((X_res**2) + (Y_res**2))**0.5/Screen_size\n",
    "        \n",
    "   \n",
    "        Prediction= Laptop_Price_Prediction_function(['Company','TypeName','Ram','Weight','Touchscreen','Ips','ppi','CPU','HDD','SSD','GPU','OS'])\n",
    "    st.success(Prediction)\n",
    "\n",
    "if __name__=='__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "d5b651c1-68f2-4725-a838-75272a19e256",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
