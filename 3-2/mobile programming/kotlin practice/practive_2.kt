import kotlin.math.sqrt

fun practice_2(){
    // lambd function은 arrow로
    val pt : (Int,Int) -> List<Int> = {x,y -> listOf(x,y) }
    println("pt function check: " + pt(1,2))

    val points: List<List<Int>> = listOf(pt(1,2),pt(-2,2),pt(-1,0),pt(2,1))
    println("points\t:"+points)

    val defaultCriteria:(List<Int>) -> Boolean = {point->true}
    println("default\t:" + myFilter(pts = points, criteria = defaultCriteria))

    val neg_x = myFilter(pts = points, criteria = {point -> point[0]<0 || point[1]<0})
    println("neg_x\t:" + neg_x)

    val close_x = myFilter(pts=points, criteria = {point -> distance(point)<=2})
    print("dist<=2\t:"+close_x)
}

fun myFilter(pts:List<List<Int>>, criteria:(List<Int>)->Boolean): List<List<Int>>{
    return pts.filter{criteria(it)}
}

fun distance(pt:List<Int>):Double{
    val (x,y) = pt
    return sqrt((x * x + y * y).toDouble())

}