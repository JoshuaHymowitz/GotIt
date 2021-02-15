from findInputSource import findInputSource
from speak import speak
from getAudio import getAudioFromMic
from getAnalysis import getAnalysis
from postToZoom import postTranscript

def main():
    #findInputSource()
    # speak('Play Recording Now')
    # keepGoing = True
    api_token = 'https://wmcc.zoom.us/closedcaption?id=2172132419&ns=Sm9zaHVhIEh5bW93aXR6J3MgUGVyc29uYWwgTWVl&expire=86400&sparams=id%2Cns%2Cexpire&signature=4D-WcDJpnp5WDykMh9-_46bV6KeCYXgjGRaW1aycfZM.AG.zW9t_ZKFvA8x7L4ys0TNsDbHospEfvcDAvlFY2BJhSw_n9eTodS8eIJnVQxRdDBjclgi4toxTlhF2BUtPCT_WxOfBCLJfPhyMvvsRiKaF6i71U1yduEqQA.iwqfupZaNPjYxCkRh9CdkA.SG83HxndEETYNTZL'

    for i in range(5):
        text = getAudioFromMic()
        getAnalysis(text)
        postTranscript(api_token, text)
    

main()
