using System;
using System.Collections;
using System.Collections.Generic;
using TMPro;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class SceneChange : MonoBehaviour
{
    public void StartToMain()
    {
        SceneManager.LoadScene("MainScene"); // ���� �̸��� MainScene���� �����ؾ� ��.
    }


    public void StartToOption()
    {
        SceneManager.LoadScene("OptionScene");
    }

    public void OptionToStart()
    {
        SceneManager.LoadScene("StartScene");
    }

    public void ToAstronaut()
    {
        SceneManager.LoadScene("AstronautExplainScene");
    }

    public void ToAlien()
    {
        SceneManager.LoadScene("AlienExplainScene");
    }
}
