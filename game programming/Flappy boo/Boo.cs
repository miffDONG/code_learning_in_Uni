using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Boo : MonoBehaviour
{
    public Rigidbody2D mRigidBody;
    // Start is called before the first frame update
    void Start()
    {
        gameObject.name = "HUFS Bird";
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            mRigidBody.velocity = Vector2.up * 6;
        }
    }
}
