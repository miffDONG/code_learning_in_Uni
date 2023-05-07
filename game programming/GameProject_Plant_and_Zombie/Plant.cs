using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Plant : MonoBehaviour
{

    public GameObject Missile;
    public float spawnRate = 2;
    private float timer = 0;
    public int HP = 7;
    private int plantHP;
    // Start is called before the first frame update
    void Start()
    {
        plantHP = HP;
    }

    // Update is called once per frame
    void Update()
    {
        if (timer < spawnRate)
        {
            timer += Time.deltaTime;
        }
        else
        {
            spawnMissile();
            timer = 0;
        }
    }
    void spawnMissile()
    {
        Instantiate(Missile, transform.position, transform.rotation);
    }
    public void TakeDamage(int damage)
    {
        plantHP -= damage;
        Debug.Log("zombie's attack");
        Debug.Log(plantHP);
        if (plantHP <= 0)
        {
            Destroy(gameObject);
        }
    }

}

