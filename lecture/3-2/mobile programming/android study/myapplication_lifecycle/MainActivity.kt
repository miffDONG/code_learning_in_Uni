package com.example.myapplication_lifecycle

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView
import org.w3c.dom.Text

/* saveInstanceState keys */
const val KEY_CNT_A = "cnt_a"
const val KEY_CNT_B = "cnt_b"

const val TAG = "MainActivity"

private var click_count_a = 0
private var click_count_b = 0
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Log.v(TAG,"onCreate called")
        setContentView(R.layout.activity_main)
        val btn_a = findViewById<Button>(R.id.btn_a)
        val btn_b = findViewById<Button>(R.id.btn_b)
        btn_a.setOnClickListener { click_a() }
        btn_b.setOnClickListener { click_b() }
        if (savedInstanceState!=null){
            val cnt_a = savedInstanceState.getInt("cnt_a",0)
            val cnt_b = savedInstanceState.getInt("cnt_b",0)

            val cnt_a_View = findViewById<TextView>(R.id.cnt_a)
            val cnt_b_view = findViewById<TextView>(R.id.cnt_b)

            cnt_a_View.text = cnt_a.toString()
            cnt_b_view.text = cnt_b.toString()
        }
    }

    override fun onStart() {
        super.onStart()
        Log.v(TAG, "onStart called")
    }

    override fun onResume() {
        super.onResume()
        Log.v(TAG, "onResume called")
    }

    override fun onPause() {
        super.onPause()
        Log.v(TAG, "onPause called")
    }

    override fun onStop() {
        super.onStop()
        Log.v(TAG, "onStop called")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.v(TAG, "onDestroy called")
    }

    override fun onRestart() {
        super.onRestart()
        Log.v(TAG, "onRestart called")
    }

    fun click_a(){
        click_count_a++
        findViewById<TextView>(R.id.cnt_a).text = click_count_a.toString()
    }
    fun click_b() {
        click_count_b++
        findViewById<TextView>(R.id.cnt_b).text = click_count_b.toString()
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        outState.putInt("cnt_a", click_count_a)
        val cnt_b = findViewById<TextView>(R.id.cnt_b)
        outState.putInt("cnt_b", cnt_b.text.toString().toInt())
    }
}