object Euler1 {
  def main(args: Array[String]) {
    val result = (1 to 1000).filter(i => List(3, 5).exists(i % _ == 0)).sum
    println(result)
  }
}
