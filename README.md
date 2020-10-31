# bert-sentence-similarity-indonesian


I'm new into Deep Learning, but i feel proud to share my first Deep Learning Web App to the world :
"A simple Web App which use BERT to identify Indonesian question/sentence/word similarity"

The technology behind this is ***Google's BERT*** and ***IndoBERT as the language model***

Hats off and claps to [Indobenchmark team](https://github.com/indobenchmark) for the IndoBERT, NLP task in Indonesian language never been easy without all of you guys :tada:


_Well honestly, what i actually do is integrating this [IndoNLU Example](https://github.com/indobenchmark/indonlu/blob/master/examples/finetune_wrete.ipynb) into [Streamlit](https://streamlit.io)_.
But yeah, whatever it is, as a new learner in Deep Learning i'm proud of myself by making my first _deep learning-based app_.


![BERT Sentence Similarity Indonesian](https://github.com/dhimasyoga16/bert-sentence-similarity-indonesian/blob/master/Web%20App.png)

## Requirements

Here are packages you'll neeed to install to make the web app works well on yours :smile:

1. **Transformers**, the technology behind this is BERT, so you'll need transformers.
2. **Streamlit**, to turn your scripts into Web App.
3. **Ngrok**, magically "expose" your local Web App into Public URL. It's free so it will give amount limit of user who's visiting your site, but it's awesome though.
4. **Git LFS**, because you need to `pull` the fine-tuned BERT model from Git LFS.

And oh, don't forget to **change Colab Runtime type into GPU**

Don't worry about how to install them, i've made tutorial for you. Keep reading.

## How to Start?

I develop this on Google Colab. So simply, you can open [this notebook](https://drive.google.com/file/d/17W53NcDs1vWzAEfayeEE8BHqRJeYHiK9/view?usp=sharing) for the tutorial & steps on how to use it.

Or you can follow these steps below as well :

1. Make sure to change you Colab runtime type to GPU.
2. Install **streamlit**. Run `!pip install streamlit`. It will ask you to restart your runtime, but **don't restart it just yet**.
3. Install **ipykernel**. Run `!pip install ipykernel~=4.10`, to reinstall the uninstalled ipykernel v4.10. Because by installing streamlit above, it will uninstall ipykernel v4.10 which is needed in Colab.
4. Install **transformers**. Run `!pip install transformers`
5. Clone this repo. Run `https://github.com/dhimasyoga16/bert-sentence-similarity.git`, and **move** into the repo folder.
6. Download a copy of **Git LFS** by running `! curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash`.

   After it's done, install it by running `!sudo apt-get install git-lfs`.
7. `Pull` the large fine-tuned model, by running `!git lfs pull`
8. Move into the `streamlit` folder (`cd streamlit`)
9. Download  **ngrok** and install it 
    ```
    !wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
    !unzip -qq ngrok-stable-linux-amd64.zip
    ```

10. Run `!streamlit run app.py &>/dev/null&`. Computer is magic. Sometimes you need to run a command you don't know what it'll do to make your things work.
11. Run 
    ```
    get_ipython().system_raw('./ngrok http 8501 &')
    ! curl -s http://localhost:4040/api/tunnels | python3 -c \
      "import sys, json; print(json.load(sys.stdin)['tunnels'][0]['public_url'])"
    ```
    Sometimes it generate `IndexError`. But don't worry, you'll just need to run it twice. Then it will generate your web app's URL.
    
    **Don't open it just yet.** Run one last command below :
    
12. Run the streamlit : `!streamlit run app.py`


Voila!

Your web app now works well just like mine :smile:

Feel free to send your issue (if any), or just sent me email if you need to ask something.
