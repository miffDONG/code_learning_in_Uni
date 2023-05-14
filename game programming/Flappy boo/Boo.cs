using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Boo : MonoBehaviour
{
    public Rigidbody2D mRigidBody;
    [SerializeField]
    public float flapStrength = 6.0f;
    public float deadZoneUp = 7;
    public float deadZoneDown = -7;

    public Logic logic;
    public bool BooIsActive;


    void Start()
    {
        gameObject.name = "HUFS Bird";
        BooIsActive = true;
        logic = GameObject.FindGameObjectWithTag("Logic").GetComponent<Logic>();
    }


    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space) && BooIsActive)
        {
            mRigidBody.velocity = Vector2.up * flapStrength;
        }

        if (transform.position.y> deadZoneUp)
        {
            logic.gameOver();
            BooIsActive = false;
        }else if (transform.position.y < deadZoneDown)
        {
            logic.gameOver();
            BooIsActive = false;
        }
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.CompareTag("Pipe"))
        {
            logic.gameOver();
            BooIsActive = false;
        }
    }

}
