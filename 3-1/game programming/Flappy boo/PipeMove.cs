using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PipeMove : MonoBehaviour
{
    public float deadZone = 20;
    public float moveSpeed = 5;

    void Start()
    {
        
    }

    void Update()
    {
        transform.position = transform.position + (Vector3.right * moveSpeed) * Time.deltaTime;

        if (transform.position.x > deadZone)
        {
            Destroy(gameObject);
        }
    }
}
