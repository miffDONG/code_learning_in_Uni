fun practice_1(){
    val students = listOf("John", "Alice", "Park", "Jessica")
    val scores = listOf(30,40,35,50)

    // task-1: print the students and their scores
    println("Student\tScore")
    println("-------\t-----")
    for ((index, score) in scores.withIndex()){
        println("${students[index]}\t ${score}")
    }
    println("-------\t-----")

    // task-2: find the average score
    var total_score = 0 //mutable set
    for ( score in scores ){
        total_score += score
    }
    println("Total Score : $total_score")

    var avg_score = total_score.toFloat()/scores.size
    println("Average Score : $avg_score")
    // task-3: find the above-average students
    val avg_above_students: MutableList<String> = mutableListOf()
    for ((index, score) in scores.withIndex()){
        if (score>avg_score){
            avg_above_students.add(students[index])
        }
    }
    print("Students above average: $avg_above_students")
}
