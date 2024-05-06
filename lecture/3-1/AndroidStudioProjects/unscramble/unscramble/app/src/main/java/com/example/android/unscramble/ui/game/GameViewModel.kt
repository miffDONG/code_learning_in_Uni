package com.example.android.unscramble.ui.game

import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class GameViewModel(value: String) : ViewModel(){
    private var _score = MutableLiveData<Int>(0)
    val score: LiveData<Int>
        get() = _score
    private var _currentWordCount = MutableLiveData<Int>(0)
    val currentWordCount: LiveData<Int>
        get() = _currentWordCount
    private var _currentScrambledWord = MutableLiveData<String>("test")
    val currentScrambledWord: LiveData<String>
        get() = _currentScrambledWord

//    private var currentWord: String = "test"
    private var currentWord: String = "test"


    init {
        getNextWord()
    }

    fun getNextWord(){
        val word = allWordsList.random().toCharArray()

        if(currentWordCount.value!!<10) {
            currentWord = String(word)
            Log.d("GameFragment", "Is Correct: $currentWord")
            word.shuffle()
            _currentScrambledWord.value = String(word)
        }
    }

    fun isPlayerWordCorrect(playerWord:String): Boolean {
        if (playerWord.equals(currentWord))
            return true
        else
            return false
    }

    fun increaseScore(){
        _score.value = _score.value!! + SCORE_INCREASE
    }
    fun increaseCount(){
        if(currentWordCount.value!!<10) {
            _currentWordCount.value = _currentWordCount.value!! + 1
        }
    }

}