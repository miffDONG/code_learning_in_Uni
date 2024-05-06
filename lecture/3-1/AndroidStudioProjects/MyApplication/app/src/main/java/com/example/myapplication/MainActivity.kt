package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView

class MainActivity : AppCompatActivity(),View.OnClickListener {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val resultTextView: TextView = findViewById(R.id.textView)
        resultTextView.text = "Hello, Android!"

        val button:Button=findViewById(R.id.button)
        button.setOnClickListener(this)

    }

    override fun onClick(v:View?){
        val resultTextView: TextView = findViewById(R.id.textView)
        resultTextView.text = "Goodbye!"
    }


}