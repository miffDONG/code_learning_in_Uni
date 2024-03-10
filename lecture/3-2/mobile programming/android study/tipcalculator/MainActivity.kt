package com.example.tipcalculator

import  androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.tipcalculator.databinding.ActivityMainBinding
import kotlin.math.round

class MainActivity : AppCompatActivity() {
    lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        binding.CalculateButton.setOnClickListener{calculate_tip()}
    }
    fun calculate_tip(){
        //cost type 변환. text->String->Double
        val cost = binding.costOfService.text.toString().toDouble()
        val opt = binding.tipOption.checkedRadioButtonId
        //when 조건문 if -> then
        val percentage = when(opt){
            binding.optTwentyPercent.id -> 0.20
            binding.optFifteenPercent.id -> 0.15
            binding.optTenPercent.id -> 0.10
            else -> 0.10
        }
        var tip_amount:Double = cost*percentage
        if(binding.RoundUpSwitch.isActivated){
            tip_amount = round(tip_amount)
        }
        binding.tipAmount.text = tip_amount.toString()
    }
}