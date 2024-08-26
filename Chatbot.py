{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPB95NNisFuywqx3avjUaG+",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jayuan101/chatbot1/blob/main/Chatbot.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit pickle"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0OASX_dMAMU3",
        "outputId": "6be4724e-bb55-4e2b-dc5d-60f8657da533"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.10/dist-packages (1.37.1)\n",
            "\u001b[31mERROR: Could not find a version that satisfies the requirement pickle (from versions: none)\u001b[0m\u001b[31m\n",
            "\u001b[0m\u001b[31mERROR: No matching distribution found for pickle\u001b[0m\u001b[31m\n",
            "\u001b[0m"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pickle\n",
        "from pathlib import Path\n",
        "import pandas as pd\n",
        "import streamlit"
      ],
      "metadata": {
        "id": "EIVcmJYosRqh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def load_file(path: str) -> str:\n",
        "    with open(path, \"rb\") as f:\n",
        "      dataset = pickle.load(f)\n",
        "    return dataset"
      ],
      "metadata": {
        "id": "WWJ2R8O1AOOP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Initialize the page\n",
        "@st.cache_data\n",
        "def load_data(folder: str)-> pd.DataFrame:\n",
        "  all_dataset = [load_file(file) for file in Path(folder).interdir()]\n",
        "  df = pd.concat (all_datasets)\n",
        "    return df"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 110
        },
        "id": "SF6E6YXN7XFc",
        "outputId": "21210ef3-77c8-4fd6-fa08-9e2373535b0c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "IndentationError",
          "evalue": "unexpected indent (<ipython-input-20-5e9782c6688f>, line 6)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-20-5e9782c6688f>\"\u001b[0;36m, line \u001b[0;32m6\u001b[0m\n\u001b[0;31m    return df\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unexpected indent\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pickle\n",
        "from pathlib import Path\n",
        "import pandas as pd\n",
        "import streamlit as st"
      ],
      "metadata": {
        "id": "XH1FrVRZseTf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def load_file(path: str) -> str:\n",
        "    with open(path, \"rb\") as f:\n",
        "      dataset = pickle.load(f)\n",
        "    return dataset"
      ],
      "metadata": {
        "id": "MKHRYg3TPfDc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "@st.cache_data\n",
        "def load_data(folder: str)-> pd.DataFrame:\n",
        "  all_dataset = [load_file(file) for file in Path(folder).interdir()]\n",
        "  df = pd.concat (all_datasets)\n",
        "  return df"
      ],
      "metadata": {
        "id": "n2xes982PiPE"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}