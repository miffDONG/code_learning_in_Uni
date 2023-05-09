using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using UnityEngine.UI;
public class Logic : MonoBehaviour
{
    public int PlayerScore;
    public Text ScoreText;

    [ContextMenu("Increase Score")]
    public void addScore()
    {
        PlayerScore = PlayerScore + 1;
        ScoreText.text = PlayerScore.ToString();
    }
}
