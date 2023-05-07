using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class zombie : MonoBehaviour
{
    public int HP = 5;
    private int zombieHP;
    public float moveSpeed = 0.3f;
    public int attack = 1;
    private Vector2 moveDirection;

    private Rigidbody2D rb;

    public GameObject plant;
    // Start is called before the first frame update
    void Start()
    {
        gameObject.tag = "zombie";
        zombieHP = HP;
        moveDirection = Vector2.left;
    }

    // Update is called once per frame
    void Update()
    {
        transform.Translate(moveDirection * moveSpeed * Time.deltaTime);
        //transform.position = transform.position + (Vector3.left*moveSpeed)*Time.deltaTime;

        rb = GetComponent<Rigidbody2D>();
    }
    public void TakeDamage(int damage)
    {
        zombieHP -= damage;

        if (zombieHP <= 0)
        {
            Die();
        }
    }

    void Die()
    {
        Destroy(gameObject);
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.CompareTag("plant"))
        {
            moveDirection = Vector2.zero;
            collision.GetComponent<Plant>().TakeDamage(attack);
            //InvokeRepeating("AttackPlant", 2f, 2f);
        }
    }
    /*
    void AttackPlant()
    {
        if (plant)
        {
            plant.GetComponent<Plant>().TakeDamage(attack); 
        }

    }
    */
    private void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.gameObject.CompareTag("plant"))
        {
            moveDirection=Vector2.left;
            //CancelInvoke();
        }
    }

    /*
    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.CompareTag("plant"))
        {
            moveDirection = Vector2.zero;
            collision.GetComponent<Plant>().TakeDamage(attack);
        }
    }
    */

    //slow effect
    //private void OnTriggerEnter2D(Collider2D collision)
    //{
    //    if (collision.gameObject.CompareTag("plant"))
    //    {
    //        collision.GetComponent<Plant>().TakeDamage(attack);        
    //        rb.AddForce(Vector2.right * 2,ForceMode2D.Impulse);
    //    }
    //}
}
